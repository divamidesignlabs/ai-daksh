---
description: Generate detailed task lists from modular epic YAML files for development implementation
globs: 
alwaysApply: false
---
# Rule: Generating a Task List from Epic Files

## Goal

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Epic YAML file. The task list should provide comprehensive implementation guidance for development teams, breaking down epic stories into actionable development tasks while maintaining cross-module integration awareness.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/tasks/implementation/`
- **Filename:** `tasks-[epic-module-name].md` (e.g., `tasks-quote-engine-core-implementation.md`)

## Process

1. **Receive Epic Reference:** The user points the AI to a specific Epic YAML file from the `/tasks/module-epics/` directory
2. **Analyze Epic Structure:** The AI reads and analyzes the complete epic structure including:
   - Module context and business priority
   - Technical specifications and architecture alignment
   - Initialization and foundation requirements
   - API layer implementation details
   - Business logic implementation components
   - Data layer implementation requirements
   - Integration layer specifications
   - Cross-module dependencies and coordination protocols
   - Testing strategy and quality assurance requirements
   - Risk management considerations
3. **Phase 1: Generate Parent Tasks:** Based on the epic analysis, create the file and generate the main, high-level implementation phases required to complete the epic. These should align with the epic's story structure (initialization, API layer, business logic, data layer, integration). Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level implementation phases based on the epic. Ready to generate the detailed sub-tasks? Respond with 'Go' to proceed."
4. **Wait for Confirmation:** Pause and wait for the user to respond with "Go"
5. **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable development sub-tasks necessary to complete the parent task. Ensure sub-tasks:
   - Map directly to epic story components and deliverables
   - Include specific technical implementation details from the epic
   - Reference cross-module dependencies and integration points
   - Include testing requirements for each implementation component
   - Consider risk mitigation strategies outlined in the epic
6. **Identify Relevant Files:** Based on the epic's output specifications and technical architecture, identify specific files that will need to be created or modified. Include:
   - Source code files with their class/component structures as specified in epic outputs
   - Test files for comprehensive coverage as outlined in testing strategy
   - Configuration files for module setup and dependencies
   - Integration files for cross-module communication
   - Documentation files for API specifications and guides
7. **Map Cross-Module Dependencies:** Extract and clearly document dependencies on other modules, including:
   - Upstream dependencies that must be completed first
   - Downstream dependencies that will consume this module's outputs
   - Integration interfaces and communication protocols
8. **Include Epic-Specific Considerations:** Add sections for:
   - Business priority and success criteria from the epic
   - Risk mitigation tasks based on epic risk management
   - Performance requirements and optimization tasks
   - Security and compliance implementation tasks
9. **Generate Final Output:** Combine all elements into the comprehensive task structure
10. **Save Task List:** Save the generated document in the `/tasks/implementation/` directory

## Input Epic Structure Understanding

The AI should understand and extract information from these epic sections:

### Epic Metadata
- **Module Context:** Primary module, related modules, business value
- **Technical Specifications:** Architecture alignment, core components
- **Business Priority:** Strategic importance, success criteria, KPIs

### Epic Story Structure
- **Initialization:** Foundation setup and module structure
- **API Layer:** Endpoint implementation and specifications
- **Business Logic:** Core service implementation and business rules
- **Data Layer:** Database design, repositories, and data management
- **Integration Layer:** External service integrations and cross-module communication

### Epic Dependencies
- **Cross-Module Dependencies:** Upstream and downstream module relationships
- **Coordination Protocols:** Event-driven communication and data consistency
- **Integration Interfaces:** API contracts and communication patterns

### Epic Outputs
- **Primary Deliverables:** Complete module components and functionality
- **Integration Outputs:** Cross-module integration capabilities
- **Documentation Outputs:** API documentation and implementation guides

### Quality Requirements
- **Testing Strategy:** Unit, integration, E2E, performance, and security testing
- **Risk Management:** Technical, business, and security risk mitigation
- **Success Metrics:** Functional, performance, and business metrics

## Output Format

The generated task list _must_ follow this structure:

```markdown
# Implementation Tasks: [Epic Module Name]

> **Epic Reference:** `/tasks/module-epics/[epic-filename].yaml`
> **Module:** [module-name]
> **Priority:** [business-priority]
> **Estimated Duration:** [duration-from-epic]
> **Team Size:** [team-size-from-epic]

## Module Overview

Brief description of the module's primary responsibility and business value from the epic context.

## Cross-Module Dependencies

### Upstream Dependencies (Must Complete First)
- **[Module Name]**: [Dependency description and interface requirements]
- **[Module Name]**: [Dependency description and interface requirements]

### Downstream Dependencies (Will Consume This Module)
- **[Module Name]**: [What they need from this module]
- **[Module Name]**: [What they need from this module]

### Integration Protocols
- [Event-driven communication requirements]
- [Data consistency requirements]
- [API contract specifications]

## Business Requirements

### Success Criteria
- [Success criteria from epic]
- [Performance targets]
- [Business metrics]

### Risk Mitigation Tasks
- [Technical risks and mitigation strategies]
- [Business risks and mitigation strategies]
- [Security risks and mitigation strategies]

## Relevant Files

### Source Code Files
- `src/modules/[module-name]/config.[ext]` - Module configuration and dependency management
- `src/modules/[module-name]/models/[entity].[ext]` - Domain entity models and business objects
- `src/modules/[module-name]/services/[service].[ext]` - Core business logic services
- `src/modules/[module-name]/api/routes.[ext]` - API endpoint handlers and routing
- `src/modules/[module-name]/api/schemas.[ext]` - Request/response schema definitions
- `src/modules/[module-name]/data/repository.[ext]` - Data access layer and repository pattern
- `src/modules/[module-name]/integrations/[integration].[ext]` - External service integrations

### Test Files
- `tests/unit/[module-name]/[component].test.[ext]` - Unit tests for individual components
- `tests/integration/[module-name]/[workflow].test.[ext]` - Integration tests for module workflows
- `tests/e2e/[module-name]/[scenario].test.[ext]` - End-to-end tests for complete user scenarios
- `tests/performance/[module-name]/[benchmark].test.[ext]` - Performance and load testing
- `tests/security/[module-name]/[security].test.[ext]` - Security and compliance testing

### Configuration Files
- `config/[module-name]/development.json` - Development environment configuration
- `config/[module-name]/staging.json` - Staging environment configuration
- `config/[module-name]/production.json` - Production environment configuration
- `docker/[module-name]/Dockerfile` - Container configuration for module deployment

### Integration Files
- `src/shared/events/[module-name]-events.[ext]` - Event schemas for cross-module communication
- `src/shared/interfaces/[module-name]-interfaces.[ext]` - API interfaces for module integration
- `docs/api/[module-name]-api-spec.yaml` - OpenAPI specification for module endpoints

### Documentation Files
- `docs/modules/[module-name]/README.md` - Module overview and setup instructions
- `docs/modules/[module-name]/api-guide.md` - API usage and integration guide
- `docs/modules/[module-name]/business-logic.md` - Business rules and logic documentation

### Notes

- **Technology Adaptation**: Use appropriate file extensions based on the technology stack:
  - `.ts` for TypeScript, `.js` for JavaScript, `.py` for Python
  - `.java` for Java, `.cs` for C#, `.go` for Go, `.rb` for Ruby
  - `.tsx/.jsx` for React components, `.vue` for Vue.js components
- **Directory Structure**: Adapt to project's established patterns:
  - Node.js: `src/`, `lib/`, `components/`
  - Python: `src/`, `app/`, package structure
  - Java: `src/main/java/`, Maven/Gradle structure
  - .NET: project folder structure with namespaces
- **Testing Frameworks**: Align with project testing standards:
  - Jest/Vitest for JavaScript/TypeScript
  - pytest for Python, JUnit for Java, NUnit for .NET
  - Cypress/Playwright for E2E testing
- **Configuration Management**: Adapt to technology-specific config:
  - `package.json` for Node.js, `requirements.txt`/`pyproject.toml` for Python
  - `pom.xml`/`build.gradle` for Java, `.csproj` for .NET
- **Integration Patterns**: Follow project-specific integration approaches:
  - REST APIs, GraphQL, gRPC, message queues, event streaming
  - Technology-specific authentication (JWT, OAuth, API keys)
- **Performance Requirements**: Validate epic-specified targets using appropriate tools:
  - Load testing with k6, JMeter, Artillery, or Locust
  - Profiling with language-specific tools
- **Security Standards**: Address compliance requirements per technology stack:
  - OWASP guidelines, dependency scanning, static analysis
  - Technology-specific security practices and tools

## Implementation Tasks

- [ ] 1.0 Module Foundation and Initialization
  - [ ] 1.1 [Sub-task for project structure setup]
  - [ ] 1.2 [Sub-task for dependency configuration]
  - [ ] 1.3 [Sub-task for environment setup]
  - [ ] 1.4 [Sub-task for basic module configuration]
- [ ] 2.0 Data Layer Implementation
  - [ ] 2.1 [Sub-task for database schema design]
  - [ ] 2.2 [Sub-task for entity model implementation]
  - [ ] 2.3 [Sub-task for repository pattern implementation]
  - [ ] 2.4 [Sub-task for data validation and constraints]
- [ ] 3.0 Business Logic Implementation
  - [ ] 3.1 [Sub-task for core service implementation]
  - [ ] 3.2 [Sub-task for business rule validation]
  - [ ] 3.3 [Sub-task for workflow orchestration]
  - [ ] 3.4 [Sub-task for error handling and logging]
- [ ] 4.0 API Layer Implementation
  - [ ] 4.1 [Sub-task for endpoint routing setup]
  - [ ] 4.2 [Sub-task for request/response schema definition]
  - [ ] 4.3 [Sub-task for authentication and authorization]
  - [ ] 4.4 [Sub-task for API documentation generation]
- [ ] 5.0 External Integration Implementation
  - [ ] 5.1 [Sub-task for upstream module integration]
  - [ ] 5.2 [Sub-task for downstream module interface]
  - [ ] 5.3 [Sub-task for external service integration]
  - [ ] 5.4 [Sub-task for event-driven communication]
- [ ] 6.0 Testing and Quality Assurance
  - [ ] 6.1 [Sub-task for unit test implementation]
  - [ ] 6.2 [Sub-task for integration test setup]
  - [ ] 6.3 [Sub-task for end-to-end test scenarios]
  - [ ] 6.4 [Sub-task for performance testing]
  - [ ] 6.5 [Sub-task for security testing]
- [ ] 7.0 Deployment and Operations
  - [ ] 7.1 [Sub-task for containerization setup]
  - [ ] 7.2 [Sub-task for CI/CD pipeline integration]
  - [ ] 7.3 [Sub-task for monitoring and alerting]
  - [ ] 7.4 [Sub-task for documentation finalization]
```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level implementation plan aligns with the epic structure and user expectations before diving into specific development details.

## Target Audience

Assume the primary readers of the task list are:
- **Development Team Lead** who will coordinate the implementation
- **Senior Developers** who will architect the technical solutions
- **Junior Developers** who will implement specific components
- **QA Engineers** who will design and execute testing strategies
- **DevOps Engineers** who will handle deployment and operations

## Epic-Specific Considerations

### Business Context Integration
- Extract and include business priority, strategic importance, and success criteria
- Map epic KPIs to specific implementation tasks
- Include business value validation checkpoints

### Technical Architecture Alignment
- Ensure tasks align with specified technology stack and frameworks
- Include architecture pattern implementation requirements
- Address performance and scalability requirements from the epic

### Cross-Module Coordination
- Clearly define dependency management tasks
- Include integration interface implementation
- Address event-driven communication setup
- Plan coordination protocol implementation

### Risk Management Integration
- Include risk mitigation tasks for identified technical risks
- Address business risk mitigation through implementation choices
- Include security risk mitigation in development tasks

### Testing Strategy Alignment
- Map epic testing requirements to specific test implementation tasks
- Include coverage targets and testing methodologies
- Address performance testing, security testing, and compliance validation

### Quality Assurance Integration
- Include code review requirements and standards
- Address compliance validation tasks
- Include documentation and runbook creation tasks

## Advanced Features

### Task Prioritization
- Mark critical path tasks based on epic business priority
- Identify dependency-blocking tasks that affect other modules
- Highlight performance-critical implementation areas

### Estimation Guidance
- Include effort estimation hints based on epic complexity
- Identify tasks that may require additional research or POCs
- Mark tasks that may need specialized expertise

### Integration Checkpoints
- Include integration testing milestones
- Define cross-module communication validation points
- Plan coordination with other module development teams

**CRITICAL:** Always extract specific technical details, file structures, class names, and method signatures from the epic's output specifications to create precise, actionable development tasks that directly implement the epic's technical vision.

## Universal Applicability Guidelines

### Technology Stack Adaptation
The template automatically adapts to different technology stacks by:
- **Extracting tech stack from epic metadata**: `project_context.technology_stack`
- **Using generic placeholders**: `[ext]`, `[module-name]`, `[component]`
- **Following epic-specified architecture patterns**: Microservices, monolithic, serverless, etc.

### Project Type Flexibility
Works across various project domains:
- **Business Applications**: E-commerce, logistics, fintech, healthcare
- **Platform Services**: Infrastructure, DevOps, analytics, monitoring
- **User Interfaces**: Web apps, mobile apps, desktop applications
- **Data Systems**: Pipelines, warehouses, real-time processing

### Framework Compatibility
Supports popular frameworks by adapting task structure:
- **Frontend**: React, Vue.js, Angular, Svelte
- **Backend**: Express/FastAPI/Spring Boot/Django
- **Mobile**: React Native, Flutter, native iOS/Android
- **Infrastructure**: Terraform, Kubernetes, Docker, cloud services

### Cross-Project Consistency
Maintains consistency while allowing customization:
- **Standard epic structure**: Initialization → Data → Business Logic → API → Integration → Testing → Deployment
- **Universal testing approach**: Unit → Integration → E2E → Performance → Security
- **Common operational concerns**: Monitoring, deployment, documentation

This template can generate implementation tasks for any epic file across different technologies, frameworks, and business domains while maintaining the structured approach and comprehensive coverage required for production-quality software development.
