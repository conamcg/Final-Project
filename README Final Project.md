# Final-Project



\# Cell Therapy Ticket Triage



An AI-powered IT ticket triage tool built for a Senior Business Systems Manager overseeing scheduling systems used in cell therapy manufacturing.



\*\*Live App:\*\* https://finalproject-connormcguire.streamlit.app/



\---



\## What It Does



Analyzes incoming IT support tickets and classifies them as \*\*ESCALATE\*\* or \*\*DELEGATE\*\* using a six-question rubric. For escalated tickets, the app automatically drafts two emails — one to the business user and one to the IT resource.



\### Triage Rubric



A ticket is escalated if any of the following are true:



1\. More than one user or site is affected

2\. The ticket describes a system bug or data error affecting multiple users

3\. The ticket contains patient, clinical, or treatment language in a disruption context

4\. The ticket requests changes to slot capacity, approval workflows, or site configuration

5\. The issue has occurred before or is recurring

6\. The ticket was submitted by a VIP user



\---



\## Features



\- \*\*Batch CSV upload\*\* — upload a CSV with `username` and `ticket` columns to triage multiple tickets at once

\- \*\*Single ticket entry\*\* — paste and triage one ticket manually

\- \*\*Email drafting\*\* — auto-generates escalation emails to the business user and IT resource for ESCALATE tickets

\- \*\*Escalation log\*\* — tracks all escalated tickets with rubric breakdown and email drafts

\- \*\*Delegation log\*\* — tracks all delegated tickets

\- \*\*Export\*\* — download either log as a formatted Excel file



\---



\## Sample Tickets



`sample\_tickets\_7.csv` is included in this repo and contains 15 realistic tickets designed to produce approximately 25% escalation rate.



\---



\## Running Locally



1\. Clone the repo

2\. Install dependencies:

&#x20;  ```

&#x20;  pip install -r requirements.txt

&#x20;  ```

3\. Set your Anthropic API key:

&#x20;  ```

&#x20;  export ANTHROPIC\_API\_KEY="your-key-here"  # Mac/Linux

&#x20;  $env:ANTHROPIC\_API\_KEY="your-key-here"    # Windows PowerShell

&#x20;  ```

4\. Run the app:

&#x20;  ```

&#x20;  python -m streamlit run streamlit\_app.py

&#x20;  ```



\---



\## Tech Stack



\- \[Streamlit](https://streamlit.io/) — UI framework

\- \[Anthropic Claude](https://www.anthropic.com/) — AI classification and email drafting (claude-haiku-4-5)

\- \[openpyxl](https://openpyxl.readthedocs.io/) — Excel export





