# Evaluation Set - IT Ticket Triage

## Ticket 1 - Normal Case (DELEGATE)
**Username:** j.martinez | **VIP:** No
**Input:** "My password expired and I can't log into the scheduling system. Can someone reset it?"
**Expected Output:** DELEGATE
**Why:** Straightforward password reset — no system knowledge required, contracted IT can handle.

---

## Ticket 2 - Normal Case (DELEGATE)
**Username:** t.nguyen | **VIP:** No
**Input:** "I was out on leave for 3 weeks and my account got locked. Can someone unlock it so I can log back in?"
**Expected Output:** DELEGATE
**Why:** Standard account reactivation request, no system expertise needed.

---

## Ticket 3 - Normal Case (DELEGATE)
**Username:** s.patel | **VIP:** No
**Input:** "Can someone set up a standard scheduler account for my new team member Sarah Johnson? She starts Monday at the Memphis site and just needs basic access."
**Expected Output:** DELEGATE
**Why:** Routine user provisioning request, contracted IT can handle standard access setup.

---

## Ticket 4 - Normal Case (DELEGATE)
**Username:** d.kim | **VIP:** No
**Input:** "The scheduling system is loading slowly on my laptop today. I restarted and it is still slow. Other apps are fine. Can IT take a look at my machine?"
**Expected Output:** DELEGATE
**Why:** Likely a local machine or browser issue, not a system bug. Contracted IT can investigate the user's device.

---

## Ticket 5 - Normal Case (DELEGATE)
**Username:** r.okonkwo | **VIP:** No
**Input:** "I accidentally deleted a manufacturing slot entry I created this morning. Is there any way to recover it?"
**Expected Output:** DELEGATE
**Why:** Standard data recovery from user error — contracted IT can restore from logs or backup without senior involvement.

---

## Ticket 6 - Escalate Case (ESCALATE)
**Username:** l.chen | **VIP:** No
**Input:** "The scheduling system is showing available manufacturing slots that were already confirmed and assigned last week. Multiple schedulers across the Atlanta and Memphis sites are seeing the same issue. We're concerned slots are being double-booked."
**Expected Output:** ESCALATE
**Why:** Potential system bug affecting data integrity across multiple sites. Double-booking manufacturing slots for cell therapies could directly impact patient treatment timelines — requires senior attention.

---

## Ticket 7 - Escalate Case (ESCALATE)
**Username:** m.rodriguez | **VIP:** No
**Input:** "We are onboarding a new manufacturing site in Denver and need the scheduling system configured to reflect our site-specific slot capacity rules and approval workflow. The standard setup does not match how our made-to-order process works."
**Expected Output:** ESCALATE
**Why:** Requires deep business system knowledge and custom configuration — not a routine IT task.

---

## Ticket 8 - Escalate Case (ESCALATE)
**Username:** a.washington | **VIP:** No
**Input:** "After this morning's system update, none of our schedulers at the Houston site can see the Q2 slot allocation data. The slots are still showing in the admin view but not in the scheduler-facing interface. We have patients waiting on treatment confirmations."
**Expected Output:** ESCALATE
**Why:** Post-update data visibility bug affecting an entire site with direct patient impact — critical escalation needed immediately.

---

## Ticket 9 - Edge Case (uncertain — likely ESCALATE)
**Username:** b.sullivan | **VIP:** No
**Input:** "The slot confirmation emails that go out to our clinical partners stopped sending yesterday. We haven't changed anything on our end. A few partners have already called asking for their confirmations."
**Expected Output:** ESCALATE (likely)
**Why:** Could be an email integration failure or a system bug. The downstream impact on clinical partners makes this time-sensitive and likely beyond contracted IT's scope — model may initially classify as DELEGATE since it doesn't involve the scheduling UI directly.

---

## Ticket 10 - Edge Case (uncertain — could go either way)
**Username:** k.thomas | **VIP:** No
**Input:** "One of our schedulers left the company last week. Can you remove her access from the scheduling system? She had admin-level permissions including the ability to override slot capacity limits."
**Expected Output:** ESCALATE (likely)
**Why:** Routine offboarding on the surface, but the admin-level permissions with capacity override access may warrant a senior review to ensure no unauthorized changes were made before departure. Model may miss this nuance and classify as a simple DELEGATE.

---

## Ticket 11 - Likely to Fail/Hallucinate/Require Human Review
**Username:** c.osei | **VIP:** Yes
**Input:** "The scheduling system approved a slot for patient therapy case #CTX-2024-8847 but our clinical team is saying the approval never came through on their end. The system log shows the approval was sent but the clinical portal shows no record of it. This is the third time this has happened this month with different patients."
**Expected Output:** ESCALATE
**Why this is likely to fail or require human review:** This ticket involves a discrepancy between two integrated systems (scheduling system and clinical portal) and references a recurring pattern across multiple patient cases. The model has no access to system logs, integration architecture, or case history — so while it may correctly classify this as ESCALATE, any reasoning it provides about the root cause will be speculative or hallucinated. A human reviewer must verify the technical details before any action is taken. This case also has direct patient safety implications, making human review non-negotiable regardless of model output.

---

## Ticket 12 - Escalate Case (ESCALATE)
**Username:** p.nguyen | **VIP:** No
**Input:** "I need to update my email address in the scheduling system. My company email changed last week and I'm not receiving system notifications anymore."
**Expected Output:** ESCALATE
**Why:** System notifications failing to deliver after an email change suggests unexpected system behavior — the system should automatically route notifications to the updated address. This may indicate a data sync issue beyond standard account management.

---

## Ticket 13 - Normal Case (DELEGATE)
**Username:** d.okafor | **VIP:** No
**Input:** "I need to request a copy of my scheduling system activity log for the past 30 days for an internal audit. Who do I contact for this?"
**Expected Output:** DELEGATE
**Why:** Standard data request for audit purposes — contracted IT can pull activity logs without senior business system knowledge.

---

## Ticket 14 - Escalate Case (ESCALATE)
**Username:** r.kim | **VIP:** No
**Input:** "I'm trying to run the standard slot utilization report but it's giving me an error saying I don't have permission. Can someone grant me access?"
**Expected Output:** ESCALATE
**Why:** Permission error on a standard report suggests unexpected system behavior — the user should already have access to a standard report. This may indicate a permissions configuration issue requiring senior review.

---

## Ticket 15 - Normal Case (DELEGATE)
**Username:** t.walker | **VIP:** No
**Input:** "I'm getting a browser error when I try to open the scheduling system on Chrome. It works fine on Edge. Can someone help me fix Chrome?"
**Expected Output:** DELEGATE
**Why:** Browser-specific issue isolated to one user's local device — contracted IT can troubleshoot Chrome without senior involvement.
