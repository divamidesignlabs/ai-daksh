---
description: "Instruction template for generating a ‘happy_flow.md’ document from project-level Markdown inputs."
globs:
  - "create-happyflow.md"
alwaysApply: false
---

# Rule: Generating a Happy Flow Document

## Goal
Guide an AI assistant to produce a `happy_flow-<project>.md` file that captures the ideal, error-free end-to-end scenario (“happy path”) for any project, using the provided vision and supporting `.md` files and following this instruction template.

## Inputs
1. **vision.md** — high-level project vision and objectives.  
2. **Supporting docs** — any additional `.md` files containing requirements, data models, UI mockups, workflows, etc.  
3. **Instruction template** — this `create-happyflow.md` file.

## Clarifying Questions
Before generating the happy flow, the AI **must** ask the user to clarify:
- **Primary Actor(s):** Who initiates and drives the main scenario?  
- **Supporting Actor(s):** What systems or roles assist (e.g., database, external APIs)?  
- **Trigger Event:** What exact event or action starts the flow?  
- **Preconditions:** What must be true or in place before the flow begins?  
- **Main Steps:** What are the sequential actions and system responses in the ideal case?  
- **Postconditions:** What final state or outputs indicate success?  
- **Business Rules (Optional):** Any domain rules or constraints to enforce?  
- **Success Criteria (Optional):** How will you measure that the flow worked (e.g., performance metrics, completion rates)?

## Process
1. **Gather Context**  
   - Read `vision.md` and all supporting `.md` files to understand domain, actors, and data.  
2. **Pose Clarifying Questions**  
   - Use the section above to elicit any missing details.  
3. **Draft Happy Flow**  
   - Populate the structure below with user answers and context from input docs.  
4. **Review & Refine**  
   - Ensure each step is clear, numbered, and describes both actor actions and system responses.  
5. **Emit File**  
   - Save as `/tasks/happy_flow-<project>.md`.

## Happy Flow Document Structure
```markdown
# 🌈 Happy Flow: <Project Name>

## 1. Purpose
One- or two-sentence statement of the ideal outcome.

## 2. Actors
- **Primary actor:** e.g., “End User”, “Admin”  
- **Supporting actors:** e.g., “Payment Gateway”, “Email Service”

## 3. Preconditions
- List bullet-wise what must be true before starting.

## 4. Trigger
- State the exact event/action that initiates this flow.

## 5. Main Flow
A **numbered** list of steps:
1. **Actor action:** Describe what the actor does.  
   **System response:** Describe how the system reacts.
2. …

## 6. Postconditions
- Bullet list of states or outputs that must hold when the flow completes.

## 7. Data / Business Rules (Optional)
- Any important rules, constraints, thresholds, or validations.

## 8. Metrics & Success Criteria (Optional)
- How will success be measured? (e.g., “Response time < 200 ms”, “> 95 % first-time success rate”.)

## 9. Open Questions (Optional)
- Any unresolved points or edge-cases needing further discussion.
```

## Output
* **Format:** Markdown (`.md`)  
* **Filename:** `create-happyflow.md`  
* **Location:** `/tasks/`

## Final Instructions
1. **Do NOT** generate the happy flow until all clarifying questions have been answered.  
2. **Always** reference the provided vision and supporting docs for context.  
3. **Keep** the happy flow focused strictly on the ideal, no-error scenario.  
4. **Ask** for additional details if any required element (actors, trigger, steps) is missing.
