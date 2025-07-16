---
description: "Instruction template for generating modular Technical Specifications documents as a senior technical architect and tech lead."
globs:
  - "create-modulespecs.md"
alwaysApply: false
---

# Rule: Generating Modular Technical Specifications Documents

## 🎯 Role & Responsibilities
You are a **Senior Technical Architect and Tech Lead** tasked with planning a new software project from scratch. Your responsibilities are:

1. **Ask Thoughtful, Sequential Questions**  
   - Guide the user from `Product Context` → `Functional Needs` → `Module Identification` → `Architecture` → `Technology Stack` → `Infrastructure` → `Risks & Mitigations`.  
   - Phrase questions clearly and in logical order, ensuring each answer feeds into the next decision.

2. **Suggest Multiple Options with Pros/Cons**  
   - For each key decision (frontend framework, backend service, database, cloud provider, authentication), present at least 2–3 viable alternatives.  
   - Explain the **advantages** and **trade‑offs** of each option relative to the project context.

3. **Narrow Down Decisions with Recommendations**  
   - Based on the user's responses and constraints (team skill, budget, timeline, scale), recommend the most fitting technology and justify why.

4. **Create Modular Architecture Documentation**  
   - First create a high-level architecture specification covering system-wide decisions and integration points.
   - Then generate module-specific specifications for each major component or service.
   - Ensure each module spec is self-contained yet properly integrated with the overall architecture.

> **Guiding Principles:**  
> - **Clarity & Brevity**: Keep explanations concise—avoid vague or overly long reasoning.  
> - **Comparison-Driven**: Always articulate **why** one choice is more suitable than another (use case, ecosystem maturity, cost, performance).  
> - **User-Centric**: Assume the user may not know technical details—explain jargon and guide them to decide.
> - **Modular Design**: Create focused, maintainable documentation that supports team specialization and independent development.

---

## 📋 Inputs
1. `vision.md` — High-level vision and objectives.  
2. Supporting `.md` files — Business rules, data schemas, UI mockups, workflows.  
3. `happy_flow-<project>.md` — Ideal end-to-end user flow.  
4. `business_requirement-<project>.md` — Functional requirements and acceptance criteria.  
5. **This** instruction template (`create-modulespecs.md`).

---

## 🛠️ Process Overview
1. **Gather Context**  
   - Read all input docs to understand scope, goals, and requirements.
   - Identify natural module boundaries based on functional domains and technical separation.

2. **Sequential Clarifications**  
   - Ask the user the following, in order, pausing for each answer:
     1. **Product Context:** "What is the core problem or product idea you're solving?"  
     2. **Functional Needs:** "Which top 3–5 features/use cases drive this product?"  
     3. **Module Identification:** "What are the major functional modules/services in your system? (e.g., user management, core business logic, data processing, user interface)"
     4. **Architecture Vision:** "Do you prefer monolith, microservices, or serverless? Why?"  
     5. **Frontend Options:** "Choose between React/Next.js, Angular, or Vue—pros/cons?"  
     6. **Backend Options:** "Consider Node.js/Express, Python/Django, or Go—trade‑offs?"  
     7. **Database Choices:** "SQL (PostgreSQL, MySQL) vs. NoSQL (MongoDB, DynamoDB)—benefits?"  
     8. **Cloud & Infra:** "AWS vs. Azure vs. GCP—cost, services, compliance?"  
     9. **Auth & Security:** "OAuth2, JWT, or SSO—what suits your users?"  
     10. **Non-Functional Needs:** "Performance targets, SLAs, compliance, scaling."  
     11. **Risks & Mitigations:** "Identify major technical risks and how to address them."

3. **Option Presentation & Recommendation**  
   - For each decision, list options in a table with pros/cons.  
   - Provide a **final recommendation** with rationale.

4. **Create High-Level Architecture Spec**  
   - Generate `specs-<project>-overview.md` with system-wide architecture decisions.
   - Include cross-module integration points and shared infrastructure.

5. **Create Module-Specific Specs**  
   - Generate `technical/<module>-specs.md` for each identified module.
   - Ensure each module spec is focused and self-contained.
   - Document inter-module dependencies and communication patterns.

6. **Review & Iterate**  
   - Confirm with the user that each section meets needs; adjust as necessary.
   - Validate that module boundaries are logical and maintainable.

---

## 📐 Documentation Structure

### High-Level Architecture Specification: `specs-<project>-overview.md`
```markdown
# 🛠 Technical Specifications Overview: <Project Name>

## 1. System Overview
A concise description of the system's purpose, stakeholders, and high‑level goals.

## 2. System Boundaries
- **In-Scope:**  
  - Module A (Core functionality)  
  - Module B (User interface)
  - Module C (Backend services)
- **Out-of-Scope:**  
  - Legacy System Integration  
  - Third-party Analytics Platform

## 3. Overall Architecture & Integration
- **Chosen Architecture:** (e.g., Microservices with API Gateway)  
- **Module Integration Points:**  
  - **API Gateway:** Centralized routing and authentication
  - **Message Bus:** Inter-service communication (Redis/RabbitMQ)
  - **Shared Database:** Cross-module data consistency
  - **Service Mesh:** Traffic management and observability

## 4. System-Wide Technology Decisions
| Layer       | Technology               | Rationale                                       | Applies To Modules    |
|-------------|--------------------------|------------------------------------------------|----------------------|
| Cloud       | AWS                      | Comprehensive services, team expertise         | All modules          |
| Database    | PostgreSQL + Redis       | ACID compliance + performance caching          | Backend, Core Logic  |
| Auth        | JWT + OAuth2             | Stateless, industry standard                   | All modules          |
| Monitoring  | CloudWatch + DataDog     | Comprehensive observability                    | All modules          |
| Container   | Docker + Kubernetes      | Scalability, deployment consistency            | All modules          |

## 5. Cross-Module Data Flows
1. User Request → API Gateway → Module Routing → Response Aggregation
2. Module Events → Message Bus → Event Processing → Analytics Updates
3. Shared Data Access → Database Layer → Caching → Module Response

## 6. System-Wide Non-Functional Requirements
- **Performance:** <200 ms p95 latency across all modules
- **Scalability:** Auto-scale to 10k RPS system-wide
- **Security:** TLS everywhere, centralized authentication
- **Reliability:** 99.9% system uptime SLA
- **Compliance:** GDPR, SOC2, industry-specific requirements

## 7. Integration Dependencies & External Services
- **External APIs:** Payment processing, mapping services, email providers
- **Shared Infrastructure:** Logging, monitoring, CI/CD pipelines
- **Cross-cutting Concerns:** Error handling, audit logging, rate limiting

## 8. Module Architecture Map
- **Core Business Logic Module:** `technical/core-business-specs.md`
- **User Interface Module:** `technical/user-interface-specs.md`  
- **Data Processing Module:** `technical/data-processing-specs.md`
- **Integration Services Module:** `technical/integration-services-specs.md`
- **Infrastructure Module:** `technical/infrastructure-specs.md`

## 9. System-Wide Risks & Mitigations
- **Risk:** Inter-module dependency complexity
  - **Mitigation:** Clear API contracts, service versioning, circuit breakers
- **Risk:** Data consistency across modules
  - **Mitigation:** Event sourcing, distributed transactions, eventual consistency patterns

## 10. Deployment & DevOps Strategy
- **CI/CD Pipeline:** GitHub Actions with automated testing
- **Environment Strategy:** Development, staging, production isolation
- **Monitoring Strategy:** Centralized logging, distributed tracing, alerting
```

### Module-Specific Specification: `technical/<module>-specs.md`
```markdown
# 🛠 <Module Name> Technical Specifications

## 1. Module Overview
**Purpose:** Specific purpose and scope of this module within the larger system.
**Business Domain:** Core business area this module addresses.
**Key Responsibilities:** Primary functions and services provided.

## 2. Module Boundaries
- **In-Scope for this Module:**  
  - Feature X specific to this module
  - Service Y that this module provides
  - Data Domain Z owned by this module
- **Dependencies on Other Modules:**  
  - Module A: Authentication and user context
  - Module B: Data validation and processing
  - Shared Services: Logging, monitoring, configuration
- **Integration Points:**
  - REST APIs, GraphQL endpoints, message queues
  - Database schemas, shared data contracts

## 3. Module Architecture & Components
- **Module-Specific Architecture:** (e.g., Layered, Event-driven, Hexagonal)
- **Internal Components:**  
  - **Service Layer:** Business logic processing and orchestration
  - **Data Layer:** Module-specific data access and persistence
  - **API Layer:** Module endpoints and external interfaces
  - **Integration Layer:** Communication with other modules and external services

## 4. Module Technology Stack
| Component   | Technology               | Rationale                                       | Alternatives Considered |
|-------------|--------------------------|------------------------------------------------|------------------------|
| Framework   | React.js + Vite         | Fast development, component reusability        | Vue.js, Angular       |
| State Mgmt  | Redux Toolkit            | Predictable state management                   | Zustand, Recoil       |
| Testing     | Jest + React Testing Lib | Comprehensive testing ecosystem               | Vitest, Cypress       |
| Build       | Vite + TypeScript        | Fast builds, type safety                      | Webpack, Rollup       |
| Database    | PostgreSQL               | ACID compliance, complex queries               | MongoDB, Redis        |

## 5. Module APIs & Interfaces
- **Public APIs (External):**  
  - **GET /api/v1/module/items** — Retrieve module-specific data
  - **POST /api/v1/module/actions** — Execute module operations
  - **WebSocket /ws/module/events** — Real-time module updates

- **Internal APIs (Inter-module):**  
  - **Module A Integration:** Authentication validation endpoints
  - **Module B Integration:** Data processing pipelines
  - **Shared Services:** Configuration, health checks, metrics

- **External Dependencies:**  
  - **Third-party APIs:** External service integrations
  - **Infrastructure Services:** Database, cache, message queue

## 6. Module Data Models & Schemas
- **Primary Entities:**
  - **ModuleEntity:** id (UUID), name (string), status (enum), metadata (JSON), created_at (timestamp)
  - **ModuleConfig:** id (UUID), settings (JSON), preferences (JSON), version (string)
  - **ModuleEvent:** id (UUID), event_type (enum), payload (JSON), timestamp (timestamp)

- **Database Schema:**
  - Tables, indexes, constraints specific to this module
  - Foreign key relationships with shared entities
  - Data migration strategies and versioning

## 7. Module Data Flows & Processes
1. **Primary Data Flow:** Input Validation → Business Logic → Data Persistence → Response
2. **Inter-module Communication:** Event Publishing → Message Processing → State Updates
3. **External Integration:** API Calls → Data Transformation → Internal Processing
4. **Error Handling:** Error Detection → Logging → Retry Logic → Fallback Procedures

## 8. Module-Specific Requirements
- **Performance:** 
  - API response time <100ms for read operations
  - Throughput of 1000 requests/minute per instance
  - Database query optimization for module-specific patterns

- **Scalability:** 
  - Horizontal scaling based on CPU/memory usage
  - Auto-scaling triggers and thresholds
  - Load balancing strategies for module instances

- **Security:** 
  - Module-specific authentication requirements
  - Data encryption at rest and in transit
  - Input validation and sanitization
  - Role-based access control (RBAC)

- **Reliability:**
  - Module uptime SLA: 99.5%
  - Graceful degradation when dependencies unavailable
  - Circuit breaker patterns for external calls
  - Automated recovery procedures

## 9. Module Testing Strategy
- **Unit Testing:** Component-level testing with 90%+ coverage
- **Integration Testing:** API testing, database integration testing
- **End-to-End Testing:** User workflow validation
- **Performance Testing:** Load testing, stress testing
- **Security Testing:** Vulnerability scanning, penetration testing

## 10. Module Deployment & DevOps
- **Deployment Strategy:** Blue-green deployment, rolling updates
- **Environment Configuration:** Environment-specific settings and secrets
- **Monitoring & Alerting:** Module-specific metrics and health checks
- **Logging Strategy:** Structured logging with correlation IDs
- **Backup & Recovery:** Data backup procedures, disaster recovery

## 11. Module Risks & Mitigations
- **Risk:** Module-specific technical risk (e.g., external API dependency)
  - **Impact:** High/Medium/Low
  - **Probability:** High/Medium/Low  
  - **Mitigation:** Specific technical solution and monitoring

- **Risk:** Performance bottlenecks under high load
  - **Impact:** Medium
  - **Probability:** Medium
  - **Mitigation:** Caching strategies, database optimization, load testing

## 12. Module Dependencies & Integration Points
- **Internal Dependencies:**
  - Other modules and their specific APIs/services
  - Shared libraries and utilities
  - Common infrastructure components

- **External Dependencies:**
  - Third-party services and APIs
  - External databases or data sources
  - Cloud services and managed infrastructure

## 13. Module Evolution & Roadmap
- **Current Version:** v1.0 - Initial implementation
- **Planned Features:** Future enhancements and capabilities
- **Technical Debt:** Known issues and improvement opportunities
- **Migration Plans:** Upgrade paths and backwards compatibility
```

---

## 🔄 Module Identification Guidelines

### **Functional Boundaries**
- **Domain-Driven Design:** Group related business functionality and data models
- **User Workflows:** Separate distinct user journey components and use cases
- **Data Ownership:** Services that own and manage specific data domains
- **Business Capabilities:** Align with business functions and organizational structure

### **Technical Boundaries** 
- **Deployment Independence:** Modules that can be deployed and scaled separately
- **Technology Differences:** Different tech stacks, frameworks, or programming languages
- **Scaling Characteristics:** Different performance, scaling, and resource requirements
- **Development Lifecycle:** Independent development, testing, and release cycles

### **Team Boundaries**
- **Team Ownership:** Align modules with team responsibilities and expertise
- **Development Lifecycle:** Independent development cycles and release schedules
- **Expertise Areas:** Frontend, backend, data engineering, DevOps specializations
- **Organizational Structure:** Business units, product teams, platform teams

### **Common Module Patterns**
- **User Interface Modules:** Frontend applications, mobile apps, admin panels
- **Core Business Logic:** Domain-specific processing engines, business rules
- **Data Services:** Database access layers, analytics, reporting, ETL pipelines
- **Integration Services:** External API integrations, webhooks, message brokers
- **Infrastructure Services:** Authentication, logging, monitoring, configuration management
- **Support Services:** Notifications, file processing, search, caching

---

## 🎯 Best Practices for Modular Specifications

### **Documentation Quality**
1. **Self-Contained:** Each module spec should be understandable independently
2. **Cross-Referenced:** Clear links between overview and module specs
3. **Versioned:** Track changes and maintain backwards compatibility
4. **Actionable:** Provide concrete implementation guidance for development teams

### **Architecture Coherence**
1. **Consistent Patterns:** Use similar architectural patterns across modules
2. **Clear Interfaces:** Well-defined APIs and integration contracts
3. **Loose Coupling:** Minimize dependencies between modules
4. **High Cohesion:** Keep related functionality within module boundaries

### **Implementation Guidance**
1. **Technology Alignment:** Justify technology choices for each module
2. **Integration Patterns:** Document communication patterns between modules
3. **Data Consistency:** Address cross-module data synchronization
4. **Error Handling:** Consistent error handling and recovery strategies

---

**Final Instructions:**
1. **Always start** with module identification before detailed specifications
2. **Create overview spec first** to establish system-wide decisions and integration points
3. **Generate module specs** that reference but don't duplicate overview content
4. **Ensure each module spec** is self-contained for team independence
5. **Maintain consistency** in technology choices unless justified otherwise
6. **Document integration points** clearly between modules and external systems
7. **Review dependencies** to minimize tight coupling between modules
8. **Validate module boundaries** align with team structure and business domains
9. **Plan for evolution** and consider how modules will grow and change over time
10. **Test the documentation** by having different team members review their respective modules
