Cell Therapy Ticket Triage
An LLM-assisted IT ticket triage tool built for a Senior Business Systems Manager overseeing scheduling systems used in cell therapy manufacturing.
Live App: https://finalproject-connormcguire.streamlit.app/

Context, User, and Problem
User: A Senior Business Systems Manager at a cell therapy manufacturing company who receives IT support tickets from master schedulers across multiple global sites. These schedulers manage access to manufacturing slots for made-to-order cell therapies — a time-critical operation where system issues can directly impact patient treatment timelines.
Workflow: The manager manually reads each incoming ticket, decides whether it warrants immediate escalation to senior IT resources or can be delegated to standard support, and if escalating, drafts two notification emails — one to the business user, one to the IT resource. This happens across a high volume of tickets with inconsistent urgency signals.
Why it matters: A missed escalation in this environment is not just an inconvenience. Scheduling system failures that go un-escalated can delay patient treatment. The manager needs a reliable, fast first-pass triage that flags the right tickets every time — not a tool that makes the final call, but one that surfaces what needs attention and drafts the communications to act on it.

Solution and Design
What It Does
Analyzes incoming IT support tickets and classifies them as ESCALATE or DELEGATE using a six-question rubric. For escalated tickets, the app automatically drafts two emails — one to the business user and one to the IT resource.
Triage Rubric
A ticket is escalated if any of the following are true:

More than one user or site is affected
The ticket describes a system bug or data error affecting multiple users
The ticket contains patient, clinical, or treatment language in a disruption context
The ticket requests changes to slot capacity, approval workflows, or site configuration
The issue has occurred before or is recurring
The ticket was submitted by a VIP user

How the AI Evaluates Tickets
Each rubric question is sent to the AI model as a separate, independent API call. The model sees the ticket and one question at a time — it has no visibility into how it answered the other five questions when making each individual judgement.
This design is intentional. A single prompt asking the model to evaluate all six criteria at once risks anchoring bias, where an early strong signal (such as obvious patient impact) colors how the model interprets later questions. By isolating each question into its own call, every criterion is evaluated on its own merits against the ticket text, producing six independent YES/NO verdicts before a final classification is made.
The model is also deliberately prompted to answer YES when in doubt. The cost asymmetry between error types makes this the right design choice: a false escalation costs a few seconds of the manager's time to review and dismiss, while a false delegation means a high-priority ticket goes unflagged — potentially leaving a critical issue unresolved for hours or days longer than it would have been had it been escalated immediately.
If any single question returns YES, the ticket is classified as ESCALATE. This mirrors how a human reviewer should work through the rubric — each item stands alone.
Key Design Choices
Model selection: Claude Haiku was chosen deliberately over larger models. Each ticket triggers 6 rubric calls plus 1 email drafting call — 7 API calls per ticket. Haiku delivers sufficient accuracy for binary YES/NO classification at a fraction of the cost and latency of Sonnet or Opus, making batch processing of many tickets practical. This is a direct cost/latency/quality trade-off.
Structured output constraints: Each rubric call uses max_tokens=10 and instructs the model to respond only YES or NO. This eliminates hallucinated reasoning in the classification step and makes the output deterministic enough to parse reliably. Email drafting uses a strict format template with exact subject line prefixes and required closing lines.
Human stays in the loop: The app never sends emails. It drafts them for review. All ESCALATE classifications are presented as recommendations. The manager makes the final call — the tool accelerates the workflow, it does not replace the judgement.

Evaluation and Results
Baseline Comparison
The baseline is the current manual process: the manager reads each ticket individually, applies the rubric from memory, decides whether to escalate, and if so drafts two emails from scratch. Dozens of tickets are submitted over the course of a week, making this a recurring and time-consuming task.
DimensionManual BaselineThis ToolTime for 15 tickets~45 minutes~75 seconds end to endTriage consistencyVariable — rubric applied from memory, fatigue and context affect judgementConsistent — same six questions applied identically to every ticketEmail draftingWritten from scratch per escalation (~5 min each)Auto-drafted instantly, ready for reviewRubric coverageRisk of skipping criteria under time pressureAll six criteria evaluated every time
At roughly 5 minutes per escalated ticket (read, decide, draft two emails) and 2 minutes per delegated ticket, manually triaging a batch of 15 tickets takes approximately 45 minutes — assuming 5 escalations and 10 delegations. The app completes the same batch in approximately 75 seconds. Across dozens of tickets per week, that compounds into hours of recovered time. The consistency gain matters equally — the rubric is applied the same way on every ticket, regardless of workload or fatigue.
Test Set
A set of 15 realistic synthetic tickets was designed to produce approximately 25% escalation rate. Tickets were crafted to test specific rubric questions — multi-site outages, patient impact language, recurring issues, VIP users — as well as clean DELEGATE cases.
Results: The model consistently identified the designed escalations. The tool is deliberately prompted to answer YES when in doubt — erring on the side of escalation rather than missing a critical ticket. This conservative bias reflects the cost asymmetry of the two error types: a false escalation costs a few seconds of the manager's time to review and dismiss, while a false delegation means a high-priority ticket goes unflagged, potentially leaving a critical issue unresolved for hours or days longer than it would have been had it been escalated immediately. In a cell therapy environment where scheduling failures can directly impact patient treatment timelines, that asymmetry makes the conservative approach the right design choice. The target escalation rate was achieved after ensuring test tickets were written with appropriately clear signal for each classification.
Where It Works

Clear multi-site or multi-user outages (Q1)
Explicit patient/clinical/treatment language (Q3)
Stated recurring history (Q5)
VIP user identification (Q6)

Where It Needs Human Review

Tickets with vague system behavior language that could be one-user or multi-user
Tickets that mention workflows or approvals in passing without requesting a config change
Nuanced cases where escalation depends on organizational context the model does not have
Email drafts always require review before sending — tone and specifics may need adjustment


Course Concepts Integrated
Model and provider selection with cost/latency/quality trade-offs
Claude Haiku was chosen over larger models after explicitly weighing cost and latency against accuracy needs. Each ticket generates 7 API calls (6 rubric + 1 email draft). Haiku handles binary YES/NO classification accurately at a fraction of the cost of Sonnet or Opus, making batch processing of many tickets practical without sacrificing triage quality.
Anatomy of an LLM call: system prompts, output constraints, structured outputs
Every rubric call uses max_tokens=10 and instructs the model to respond only YES or NO — eliminating verbose reasoning in the classification step and making outputs reliable enough to parse programmatically. Email drafting uses a strict format template with required subject line prefixes and a mandatory closing sentence. A shared system prompt establishes the business context (cell therapy manufacturing, patient scheduling stakes) for every call.
Context engineering
The system prompt provides domain-specific context that the model could not infer on its own — what master schedulers do, why slot access is time-critical, and what the organizational stakes are. This context is passed on every call so the model evaluates tickets against the right frame of reference rather than a generic IT support context.
Evaluation design: rubrics, test sets, baselines
A 15-ticket synthetic test set was built specifically to evaluate the tool against a target escalation rate. Tickets were designed to hit specific rubric questions and cleanly avoid others. Results were compared against the manual baseline on accuracy, consistency, and time. The tool is prompted to answer YES when uncertain, reflecting a deliberate design choice to prioritize catching critical tickets over minimizing escalation volume.
Governance and deployment controls: human review, action limits, logging
The app never sends emails automatically. All classifications are framed as recommendations. The manager reviews every draft before acting. Escalation and delegation logs are maintained within the session and exportable for audit. The system is explicitly designed so that a human makes every consequential decision — the tool accelerates the workflow, it does not replace the judgement.

Features

Batch CSV upload — upload a CSV with username and ticket columns to triage multiple tickets at once
Single ticket entry — paste and triage one ticket manually
Rubric breakdown — every ticket shows the YES/NO result for each of the six criteria
Email drafting — auto-generates escalation emails to the business user and IT resource for ESCALATE tickets
One-click email — each escalated ticket has Email Business User and Email IT Resource buttons that open a pre-populated draft in your default mail client, ready to review and send
Remove — remove any individual ticket from the escalation or delegation log without clearing the rest
Escalation log — tracks all escalated tickets with rubric breakdown and email drafts
Delegation log — tracks all delegated tickets
Export — download either log as a formatted Excel file
Clear All — wipe the escalation or delegation log entirely to start fresh


Sample Tickets
sample_tickets_7.csv is included in this repo and contains 15 realistic synthetic tickets designed to produce approximately 25% escalation rate. Use this file to run a representative batch through the app.

Setup and Usage
Running on Streamlit Cloud
The app is live at https://finalproject-connormcguire.streamlit.app/ — no installation required. To provide an API key for grading, add it under App Settings → Secrets in Streamlit Cloud with the key ANTHROPIC_API_KEY.
Running Locally

Clone the repo
Install dependencies with pip install -r requirements.txt
Set your Anthropic API key — on Windows PowerShell: $env:ANTHROPIC_API_KEY="your-key-here" or on Mac/Linux: export ANTHROPIC_API_KEY="your-key-here"
Run with python -m streamlit run streamlit_app.py
Upload sample_tickets_7.csv using the Batch CSV Upload tab to see a full triage run


Artifact Snapshot
Full App — Rubric, Escalation Log, Delegation Log
Show Image
The app displays the full 6-question triage rubric on the left, with the batch CSV upload and single ticket tabs on the right. After processing, escalated and delegated tickets appear in separate logs below with timestamps and summaries.
Escalated Ticket — Rubric Breakdown and Auto-Drafted Emails
Show Image
An expanded escalation entry showing the ticket text, YES/NO verdict for each rubric criterion, and two auto-drafted emails ready for the manager to review — one to the business user, one to the IT resource. This ticket (n.okafor) triggered Q1, Q2, Q3, and Q4 — multiple US sites down with patient appointment impact.

Tech Stack

Streamlit — UI framework
Anthropic Claude — LLM classification and email drafting (claude-haiku-4-5)
openpyxl — Excel export