import anthropic
import os

# Your API key
API_KEY = os.environ.get("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=API_KEY)

# VIP users list
VIP_USERS = {"c.osei"}

# Rubric questions — each evaluated in isolation
RUBRIC_QUESTIONS = [
    "Does the ticket explicitly name or describe more than one user or more than one site as being affected? Answer only YES or NO. If you are uncertain, answer YES.",
    "Does the ticket describe system behavior that contradicts what the system is supposed to do, such as showing wrong data, failing to send, or behaving differently after an update, affecting multiple users or the system as a whole — not just one user's browser or local device? Answer only YES or NO. If you are uncertain, answer YES.",
    "Does the ticket contain the words 'patient', 'clinical', or 'treatment' in a context that describes a current disruption? Answer only YES or NO. If you are uncertain, answer YES.",
    "Does the ticket explicitly request changes to slot capacity rules, approval workflows, or site-specific system configuration — not standard user account creation or access provisioning? Answer only YES or NO. If you are uncertain, answer YES.",
    "Does the ticket explicitly state that the same issue has happened before or is happening repeatedly? Answer only YES or NO. If you are uncertain, answer YES.",
]

RUBRIC_LABELS = [
    "Multiple users or sites",
    "System bug or data error",
    "Patient or clinical impact",
    "Custom config or deep knowledge",
    "Recurring issue or pattern",
    "VIP user",
]

SYSTEM_CONTEXT = """You are an IT ticket triage assistant supporting a Senior Business
Systems Manager who oversees scheduling systems used by master schedulers at
manufacturing sites. These schedulers manage access to manufacturing slots for
made-to-order cell therapies — a time-critical, high-stakes operation where
system issues can directly impact patient treatment timelines."""

EMAIL_PROMPT = """You are drafting two very short, professional emails for an escalated IT support ticket.

Context about the ticket:
TICKET: {ticket}

Rubric findings:
{rubric_summary}

Draft two succinct emails:

EMAIL 1 - TO BUSINESS USER (from contracted IT team):
- Acknowledge receipt
- Confirm escalation to senior management
- Confirm IT is their point of contact
- One short paragraph max

EMAIL 2 - TO IT RESOURCE:
- Summarize the issue in one sentence
- Note senior manager oversight
- Flag any patient/clinical urgency if applicable
- Final line must say exactly: "Please provide a status update within the next two hours."

Respond in this exact format:

EMAIL 1 - TO BUSINESS USER:
Subject: [subject line]
Body:
[email body]

EMAIL 2 - TO IT RESOURCE:
Subject: [subject line]
Body:
[email body]
"""

def ask_rubric_question(ticket, question):
    """Make a single API call for one rubric question."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=10,
        system=SYSTEM_CONTEXT,
        messages=[
            {"role": "user", "content": f"Ticket:\n{ticket}\n\nQuestion: {question}"}
        ]
    )
    answer = message.content[0].text.strip().upper()
    # If response doesn't start with YES or NO, default to YES
    if not answer.startswith("YES") and not answer.startswith("NO"):
        return "YES"
    return "YES" if answer.startswith("YES") else "NO"

def draft_emails(ticket, rubric_answers):
    """Make a single API call to draft both emails."""
    rubric_summary = "\n".join(
        f"- {RUBRIC_LABELS[i]}: {rubric_answers[i]}"
        for i in range(len(rubric_answers))
    )
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        system=SYSTEM_CONTEXT,
        messages=[
            {"role": "user", "content": EMAIL_PROMPT.format(
                ticket=ticket,
                rubric_summary=rubric_summary
            )}
        ]
    )
    return message.content[0].text

def triage_ticket(ticket, username):
    """Run full rubric triage for a single ticket."""
    rubric_answers = []

    # Calls 1-5: rubric questions
    for question in RUBRIC_QUESTIONS:
        answer = ask_rubric_question(ticket, question)
        rubric_answers.append(answer)

    # Call 6: VIP check (local, no API call needed)
    is_vip = "YES" if username.lower() in VIP_USERS else "NO"
    rubric_answers.append(is_vip)

    # Aggregate: any YES = ESCALATE
    classification = "ESCALATE" if "YES" in rubric_answers else "DELEGATE"

    return classification, rubric_answers

# Tickets with synthetic usernames and VIP tags
tickets = [
    ("j.martinez", "My password expired and I can't log into the scheduling system. Can someone reset it?"),
    ("t.nguyen", "I was out on leave for 3 weeks and my account got locked. Can someone unlock it so I can log back in?"),
    ("s.patel", "Can someone set up a standard scheduler account for my new team member Sarah Johnson? She starts Monday at the Memphis site and just needs basic access."),
    ("d.kim", "The scheduling system is loading slowly on my laptop today. I restarted and it's still slow. Other apps are fine. Can IT take a look at my machine?"),
    ("r.okonkwo", "I accidentally deleted a manufacturing slot entry I created this morning. Is there any way to recover it?"),
    ("l.chen", "The scheduling system is showing available manufacturing slots that were already confirmed and assigned last week. Multiple schedulers across the Atlanta and Memphis sites are seeing the same issue. We're concerned slots are being double-booked."),
    ("m.rodriguez", "We are onboarding a new manufacturing site in Denver and need the scheduling system configured to reflect our site-specific slot capacity rules and approval workflow. The standard setup does not match how our made-to-order process works."),
    ("a.washington", "After this morning's system update, none of our schedulers at the Houston site can see the Q2 slot allocation data. The slots are still showing in the admin view but not in the scheduler-facing interface. We have patients waiting on treatment confirmations."),
    ("b.sullivan", "The slot confirmation emails that go out to our clinical partners stopped sending yesterday. We haven't changed anything on our end. A few partners have already called asking for their confirmations."),
    ("k.thomas", "One of our schedulers left the company last week. Can you remove her access from the scheduling system? She had admin-level permissions including the ability to override slot capacity limits."),
    ("c.osei", "The scheduling system approved a slot for patient therapy case #CTX-2024-8847 but our clinical team is saying the approval never came through on their end. The system log shows the approval was sent but the clinical portal shows no record of it. This is the third time this has happened this month with different patients."),
    ("p.nguyen", "I need to update my email address in the scheduling system. My company email changed last week and I'm not receiving system notifications anymore."),
    ("d.okafor", "I need to request a copy of my scheduling system activity log for the past 30 days for an internal audit. Who do I contact for this?"),
    ("r.kim", "I'm trying to run the standard slot utilization report but it's giving me an error saying I don't have permission. Can someone grant me access?"),
    ("t.walker", "I'm getting a browser error when I try to open the scheduling system on Chrome. It works fine on Edge. Can someone help me fix Chrome?"),
]

# Run triage
results = []

for i, (username, ticket) in enumerate(tickets, 1):
    print(f"\n--- Ticket {i} ({username}) ---")
    print(f"INPUT: {ticket}")
    print("Running rubric...")

    classification, rubric_answers = triage_ticket(ticket, username)

    # Print rubric results
    for j, label in enumerate(RUBRIC_LABELS):
        print(f"  {label}: {rubric_answers[j]}")

    print(f"CLASSIFICATION: {classification}")

    result_lines = [
        f"--- Ticket {i} ({username}) ---",
        f"INPUT: {ticket}",
        "",
        "RUBRIC:",
    ]
    for j, label in enumerate(RUBRIC_LABELS):
        result_lines.append(f"  {label}: {rubric_answers[j]}")
    result_lines.append(f"\nCLASSIFICATION: {classification}")

    # Draft emails only for ESCALATE
    if classification == "ESCALATE":
        print("Drafting emails...")
        emails = draft_emails(ticket, rubric_answers)
        print(f"\n{emails}")
        result_lines.append(f"\n{emails}")

    result_lines.append("\n" + "=" * 60)
    results.append("\n".join(result_lines))

# Save results
with open("output.txt", "w") as f:
    f.write("\n".join(results))

print("\n✓ All tickets processed. Results saved to output.txt")
