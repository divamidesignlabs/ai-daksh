---
description: "Instruction template for generating a ‘business_requirement.md’ document from project-level Markdown inputs including vision, supporting docs, and happy flow."
globs:
  - "create-business_requirement.md"
alwaysApply: false
---

# Rule: Generating a Business / Functional Requirements Document

## Goal
Guide an AI assistant to produce a `business_requirement-<project>.md` file that captures the detailed business and functional requirements—including key use cases and acceptance criteria—for any project, based on provided vision, supporting documentation, and the project’s happy flow.

## Inputs
1. **vision.md** — high-level project vision and objectives.  
2. **Supporting docs** — additional `.md` files containing background, data models, UI mockups, workflows, etc.  
3. **happy_flow-<project>.md** — the ideal end-to-end scenario document.  
4. **Instruction template** — this `create-business_requirement.md` file.

## Clarifying Questions
Before drafting the requirements, the AI **must** ask:
- **Stakeholders:** Who are the primary and secondary stakeholders?  
- **Scope:** What is in- and out-of-scope for this document?  
- **Use Cases:** What are the key business use cases?  
- **Functional Requirements:** What specific capabilities must the system provide?  
- **Acceptance Criteria:** What conditions must be met to consider each requirement done?  
- **Non-Functional Requirements:** Are there performance, security, or reliability constraints?  
- **Priority:** Which requirements are high, medium, or low priority?  
- **Dependencies:** Any upstream/downstream systems or data dependencies?  

## Process
1. **Gather Context**  
   - Read `vision.md`, supporting docs, and `happy_flow-<project>.md`.  
2. **Pose Clarifying Questions**  
   - Use the section above to elicit missing details.  
3. **Draft Requirements**  
   - Fill in the structure below with content derived from inputs and answers.  
4. **Review & Refine**  
   - Ensure clarity, correct numbering, and alignment with the happy flow.  
5. **Emit File**  
   - Save as `/tasks/business_requirement-<project>.md`.

## Business / Functional Requirements Document Structure

```markdown
# 📄 Business & Functional Requirements: <Project Name>

## 1. Purpose
One- or two-sentence description of the document’s intent.

## 2. Scope
- **In-Scope:**  
  - Bullet items  
- **Out-of-Scope:**  
  - Bullet items

## 3. Stakeholders
- **Primary:** e.g. “Product Owner”, “End Users”  
- **Secondary:** e.g. “Support Team”, “External API Provider”

## 4. Key Use Cases
For each use case:
- **Use Case UC-<number>: <Title>**  
  **Description:** Brief summary.  
  **Actors:** List of actors.  
  **Preconditions:** What must be true before.  
  **Main Flow:** Numbered steps describing the ideal path.  
  **Alternate Flows:** Bullet or numbered list of variations.

## 5. Functional Requirements
Numbered list of functional requirements:
1. **FR-<number>:** Description of the capability.  
2. ...

## 6. Acceptance Criteria
For each FR or Use Case:
- **FR-<number> / UC-<number>:**  
  - AC1: Criterion one.  
  - AC2: Criterion two.

## 7. Non-Functional Requirements (Optional)
- **Performance:** e.g., “Response time < 200 ms”  
- **Security:** e.g., “Data encrypted at rest”  
- **Reliability:** e.g., “99.9% uptime”

## 8. Data Models & Entities (Optional)
- **Entity Name:** Attributes and relationships.  
- ...

## 9. Business Rules & Constraints (Optional)
- Rule 1: Description.  
- Rule 2: Description.

## 10. Assumptions & Dependencies (Optional)
- **Assumptions:** e.g., “User has valid account”.  
- **Dependencies:** e.g., “External Payment API available”.

## 11. Glossary (Optional)
- **Term:** Definition.

## 12. Open Questions (Optional)
- List any unresolved issues or clarifications needed.
```

## Output
* **Format:** Markdown (`.md`)  
* **Filename:** `create-business_requirement.md`  
* **Location:** `/tasks/`

## Final Instructions
1. **Do NOT** draft the requirements until all clarifying questions are answered.  
2. **Ensure** each requirement maps back to vision, supporting docs, or happy flow.  
3. **Maintain** consistency in numbering (UC-001, FR-001, AC-001).  
4. **Ask** for missing details if any section lacks information.
