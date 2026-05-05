\# Project Plan: IT Support Ticket Triage and Communication Assistant



\---



\## 1. Project Title

IT Support Ticket Triage and Communication Assistant for 

Manufacturing Business Systems



\---



\## 2. Target User, Workflow, and Business Value



\*\*Who the user is:\*\*

A Senior Business Systems Manager who oversees scheduling systems 

used by master schedulers at manufacturing sites. These schedulers 

manage access to manufacturing slots for made-to-order cell therapies 

— a time-critical, high-stakes operation where system issues can 

directly impact patient treatment timelines.



\*\*What recurring task or decision is being improved:\*\*

The manager receives dozens of IT support tickets daily from 

schedulers across multiple manufacturing sites. Each ticket must be 

read, assessed, and routed — either escalated for senior attention 

or delegated to contracted IT resources. For escalated tickets, 

the manager must also ensure timely communication is sent to both 

the business user and the IT resource handling the issue.



\*\*Where the workflow begins and ends:\*\*

The workflow begins when a business user submits a support ticket. 

It ends when the ticket has been classified as Escalate or Delegate, 

and — for escalated tickets — two draft emails have been generated: 

one to the business user acknowledging the issue and one to the 

contracted IT resource outlining the problem and response expectations.



\*\*Why better performance on this workflow matters, and to whom:\*\*

Manual triage is time-consuming and inconsistent. In a 

patient-critical manufacturing environment, delays in identifying 

and escalating high-priority tickets can disrupt treatment schedules. 

Automating first-pass triage frees the senior manager to focus on 

issues that genuinely require their expertise, while ensuring 

schedulers receive timely, professional communication about the 

status of their reported issues.



\---



\## 3. Problem Statement and GenAI Fit



\*\*The exact task:\*\*

Given a raw support ticket submitted by a manufacturing site 

scheduler, the system classifies the ticket as Escalate or Delegate 

and — for escalated tickets — drafts two stakeholder emails with 

consistent tone, role representation, and response time expectations.



\*\*What part of the workflow benefits from language models:\*\*

Ticket triage requires reading comprehension, contextual judgment, 

and natural language generation — all tasks well suited to language 

models. The system must understand the difference between a routine 

access request and a multi-site data integrity failure, and must 

generate professional emails that accurately represent the roles of 

the senior manager, contracted IT, and the business user.



\*\*Why a simpler non-GenAI tool would not be enough:\*\*

The current manual process requires the senior manager to read and 

classify every ticket individually, which is time-consuming and 

inconsistent at scale. A language model is necessary to handle the 

reading comprehension, contextual judgment, and email drafting 

requirements of this workflow in a way that manual review cannot 

match for volume and speed.



\---



\## 4. Planned System Design and Baseline



\*\*Expected workflow and architecture:\*\*

The user opens a Streamlit web app in their browser and submits 

tickets either one at a time or as a batch CSV upload. The app 

sends each ticket to the Anthropic API with a structured system 

prompt that defines the triage logic and email drafting 

requirements. The model returns a structured response containing 

the classification, a reason, and — for escalated tickets — two 

draft emails. The app displays all outputs clearly in separate 

labeled sections and maintains a running Escalation Log for 

senior manager review.



\*\*Two course concepts and how they show up:\*\*



1\. Anatomy of an LLM call: system prompts, temperature, output 

constraints, and structured outputs (Week 2-3):

The system prompt explicitly defines classification criteria, 

role boundaries, email tone requirements, and a required output 

format that the model must follow for every ticket. Temperature 

will be set low (0.2) to prioritize consistency and 

reproducibility over creativity, which is appropriate for a 

triage and communication workflow. The output format will be 

enforced through prompt constraints requiring labeled sections 

(CLASSIFICATION, REASON, EMAIL 1, EMAIL 2) so the app can 

parse and display results reliably.



2\. Evaluation design: rubrics, test sets, baselines, and 

model-as-judge (Week 6):

The system will be evaluated against a formal rubric covering 

four dimensions: classification accuracy, role representation 

accuracy in emails, tone appropriateness, and consistency of 

response time expectations. The evaluation set will contain at 

least 15 tickets including normal cases, escalation cases, edge 

cases, and cases designed to surface hallucination or 

misclassification. Results will be compared against the manual 

baseline. A model-as-judge approach will be used to score 

email quality at scale, supplemented by manual spot checks.



\*\*Simpler baseline to compare against:\*\*

The baseline is the current manual process — the senior manager 

reads each ticket individually and makes a classification 

decision without any technological assistance. This baseline 

reflects the real alternative the system is replacing. The 

comparison will measure whether the GenAI system matches or 

improves on the manager's own classification accuracy, and will 

also evaluate time savings — specifically how long manual triage 

takes per ticket versus automated triage at scale.



\*\*The app the user sees and does:\*\*

The user opens a Streamlit app in their browser. They have two 

options for submitting tickets:



Option 1 - Single ticket: The user pastes one support ticket 

into a text input field and clicks Submit to get an instant 

classification and email drafts.



Option 2 - Batch upload: The user uploads a CSV file containing 

multiple tickets at once. Each row in the CSV represents one 

ticket. The app processes all tickets automatically and displays 

results for each one in sequence.



For both options, the results panel displays the classification 

(Escalate or Delegate) with a brief reason, and — for escalated 

tickets — two clearly labeled draft emails that the manager can 

review and send.



The app also maintains a running Escalation Log — a cumulative 

list of all tickets classified as Escalate during the session. 

This log displays each escalated ticket in order of submission, 

showing the ticket summary, classification reason, and timestamp. 

The senior manager can use this log as a live review queue to 

track which issues require their attention. The full session 

results including the escalation log can be exported as a text 

file for record keeping.



The interface is minimal and designed for speed, reflecting the 

high-volume nature of the triage workflow.



\---



\## 5. Evaluation Plan



\*\*What success looks like:\*\*

The system correctly classifies at least 90% of tickets in the 

evaluation set, produces emails that accurately represent the 

roles of all stakeholders, maintains a consistent and professional 

tone appropriate for a patient-critical environment, and always 

includes the required two-hour status update requirement in IT 

resource emails.



\*\*What will be measured:\*\*

\- Classification accuracy: does the system correctly Escalate 

&#x20; or Delegate each ticket?

\- Role representation accuracy: do emails correctly position 

&#x20; contracted IT as the point of contact and the senior manager 

&#x20; as oversight?

\- Tone appropriateness: are emails professional and appropriately 

&#x20; urgent given the patient-critical context?

\- Output consistency: does the system always follow the required 

&#x20; output format and include the two-hour status update line?

\- Time savings: how long does manual triage take per ticket 

&#x20; versus automated triage at scale?



\*\*Test set:\*\*

At least 15 tickets including normal delegate cases, clear 

escalation cases, edge cases, and cases designed to surface 

hallucination or misclassification. This expands the 11-case 

evaluation set built during HW2.



\*\*Baseline comparison method:\*\*

The senior manager will manually classify each ticket in the 

evaluation set without any technological assistance, recording 

their classification and the time taken per ticket. The GenAI 

system will process the same tickets and results will be compared 

across three dimensions: classification agreement, time to 

triage, and — for escalated tickets — quality of draft emails 

versus manually written communications. Email quality will be 

scored using a model-as-judge rubric supplemented by manual 

spot checks.



\---



\## 6. Example Inputs and Failure Cases



\*\*Example inputs:\*\*



1\. "My password expired and I can't log into the scheduling 

system. Can someone reset it?"

Expected: DELEGATE — routine password reset.



2\. "The scheduling system is showing available manufacturing 

slots that were already confirmed and assigned last week. 

Multiple schedulers across the Atlanta and Memphis sites are 

seeing the same issue. We're concerned slots are being 

double-booked."

Expected: ESCALATE — potential data integrity bug affecting 

multiple sites with patient impact.



3\. "We are onboarding a new manufacturing site in Denver and 

need the scheduling system configured to reflect our 

site-specific slot capacity rules and approval workflow."

Expected: ESCALATE — requires deep system knowledge and 

custom configuration.



4\. "The report I run every Monday is taking much longer than 

usual — about 45 minutes instead of 5. Nothing has changed 

on my end."

Expected: ESCALATE (likely) — could indicate a system 

performance issue but is ambiguous.



5\. "One of our schedulers left the company last week. Can you 

remove her access from the scheduling system? She had 

admin-level permissions including the ability to override 

slot capacity limits."

Expected: DELEGATE (likely) — but the admin-level permissions 

may warrant a senior review that the model could miss.



\*\*Anticipated failure cases:\*\*



1\. Ambiguous performance issues: tickets describing slowdowns 

or delays that could indicate either a local device problem 

or a system-wide bug. The model may inconsistently classify 

these depending on phrasing.



2\. Security-sensitive offboarding: tickets involving departing 

users with elevated permissions that look routine on the 

surface but carry implicit security risk. The model is likely 

to miss this nuance without explicit prompt guidance.



3\. Cross-system integration failures: tickets referencing 

discrepancies between two integrated systems where the model 

has no access to system logs or architecture context. Any 

root cause reasoning the model provides will be speculative 

and should be flagged for human review.



\---



\## 7. Risks and Governance



\*\*Where the system could fail:\*\*

\- Misclassifying an escalation-worthy ticket as Delegate, 

&#x20; causing a critical issue to go unreviewed by senior management

\- Generating emails that misrepresent roles or response 

&#x20; expectations, causing confusion among stakeholders

\- Producing speculative root cause reasoning in emails for 

&#x20; tickets involving complex system interactions



\*\*Where it should not be trusted:\*\*

\- The system should never make a final routing decision without 

&#x20; human review of escalated tickets

\- Email drafts should always be reviewed before sending — they 

&#x20; are drafts, not final communications

\- The system should not be trusted on tickets involving 

&#x20; patient safety implications without mandatory senior 

&#x20; manager review



\*\*Controls, refusal rules, and human-review boundaries:\*\*

\- All ESCALATE classifications require senior manager review 

&#x20; before any action is taken

\- DELEGATE classifications should be spot-checked weekly by 

&#x20; IT leadership to catch misclassifications

\- The app will include a visible disclaimer on every output 

&#x20; stating that results require human review before action

\- No automated sending of emails — all drafts require manual 

&#x20; approval



\*\*Data, privacy, and cost concerns:\*\*

\- Only synthetic or anonymized ticket data will be used in 

&#x20; development and evaluation

\- No real patient identifiers, case numbers, or PII will be 

&#x20; committed to the repository

\- API costs are expected to remain minimal given the short 

&#x20; input and output length of each ticket

\- The API key will be managed via environment variables and 

&#x20; never committed to the repository



\---



\## 8. Plan for the Week 6 Check-In



By the Week 6 check-in I expect to have the following in place:



\*\*App:\*\*

A working Streamlit app that accepts either a single ticket 

or a batch CSV upload, makes real API calls to the Anthropic 

API, and displays the classification, reason, and draft emails 

in clearly labeled sections. The Escalation Log will be 

functional and exportable. The system prompt will be at its 

final or near-final version based on prompt iteration from HW2.



\*\*Evaluation:\*\*

An expanded evaluation set of at least 15 tickets with ground 

truth labels. A formal scoring rubric covering classification 

accuracy, role representation, tone, and output consistency. 

Initial results from running the eval set through both the 

GenAI system and the manual baseline.



\*\*Baseline comparison:\*\*

The senior manager will have manually classified all 15 

evaluation set tickets without technological assistance, 

recording classification decisions and time taken per ticket. 

Initial comparison results between manual triage and the 

GenAI system will be documented.

