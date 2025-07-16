---
description: Generate focused, modular project epics based on technical specifications (Universal Template)
globs:
alwaysApply: false
---
# Rule: Generating Modular Project Epics Document (Universal Template)

## Goal

To guide an AI assistant in creating focused Project Epics Documents in YAML format for any modular system, where each epic corresponds to a specific module or system component. The epics should leverage detailed technical specifications and clearly document cross-module dependencies and integration points.

## Enhanced Modular Approach

### Key Principles
- **One Epic Per Module**: Each epic focuses on a single module's functionality
- **Technical Specification Alignment**: Stories map directly to technical components from module specs
- **Cross-Module Dependencies**: Explicit documentation of inter-module dependencies
- **Integration Coordination**: Separate coordination epic for cross-cutting concerns
- **Specification Traceability**: Direct references to technical specification documents

### Benefits
🎯 **Better Epic Quality**: Each epic has focused technical context
📋 **Clear Dependencies**: Dependencies between modules are explicit
🔗 **Component Mapping**: User stories map directly to technical components
⚡ **Faster Development**: Teams can work independently on focused modules
🔍 **Better Testing**: Module-specific test coverage and validation

## Process

1. **Receive Initial Prompt**: The user provides a brief description or request for new project epics or functionality along with the epic-name. If not given, ask for the epic-name and target module.
2. **Analyze Module Specifications**: Review the project's technical documentation folder and module-specific specification documents to understand module architecture, dependencies, and technical requirements.
3. **Identify Module Boundaries**: Determine which module(s) the epic targets and identify cross-module integration points.
4. **Ask Clarifying Questions**: Before writing the epics document, the AI *must* ask clarifying questions focused on module-specific concerns and cross-module dependencies.
5. **Generate Modular Epics Document**: Create focused epics that align with module specifications and technical architecture.
6. **Save Epics Document**: Save as `epic-{module-name}-{epic-name}.yaml` in `/tasks/` directory.

## Thinking and Guiding Principles

Before generating the modular epics document, consider these enhanced principles:

### Module-Specific Principles
- **Technical Specification Alignment**: Stories should directly implement components defined in module specs
- **API Contract Focus**: Clear definition of module API boundaries and contracts
- **Module Independence**: Stories should be implementable within module boundaries
- **Performance Requirements**: Include module-specific performance and scalability requirements
- **Security Context**: Module-specific security concerns and authentication patterns

### Cross-Module Principles
- **Dependency Mapping**: Explicit mapping of upstream/downstream module dependencies
- **Integration Patterns**: Clear definition of communication patterns between modules
- **Data Flow Documentation**: Document data flow across module boundaries
- **Event Handling**: Define event-driven communication between modules
- **Shared Resource Management**: Handle shared databases, caches, and external services

## Enhanced Clarifying Questions

The AI should adapt questions based on project context, module specifications, and technical architecture:

### Project Context Discovery
- **Project Type**: "What type of system is this project? a) Web Application b) Mobile Application c) API Platform d) Data Processing System e) IoT Platform f) E-commerce Platform g) Enterprise Software h) Other (please specify)"
- **Technology Stack**: "What is the primary technology stack? a) JavaScript/Node.js b) Python/Django/Flask c) Java/Spring d) .NET/C# e) Go f) Ruby on Rails g) PHP h) Mixed/Microservices i) Other"
- **Architecture Pattern**: "What architectural pattern does the project follow? a) Monolithic b) Microservices c) Serverless d) Event-driven e) Layered architecture f) Hexagonal/Clean architecture g) Other"

### Module Identification
- **Module Discovery**: "Please list the main modules/components in your system. If you have technical specifications, reference them. Common patterns include: Frontend, Backend API, Database Layer, Authentication, Business Logic, Integration Layer, Analytics, Infrastructure"
- **Target Module**: "Which module is this epic primarily focused on? Please specify from your project's module list or indicate if this is a new module"
- **Module Scope**: "What specific components within the module need to be implemented? (Reference the module's technical specification if available)"
- **Integration Level**: "Does this epic require integration with other modules? If yes, which ones and what type of integration?"

### Technical Context
- **Architecture Alignment**: "Which technical layers/components should this epic implement? a) Presentation Layer b) API/Service Layer c) Business Logic Layer d) Data Access Layer e) External Integrations f) Infrastructure Components g) All layers h) Custom components"
- **Performance Requirements**: "What are the specific performance requirements? a) Response time targets (specify) b) Throughput requirements (specify) c) Availability targets (specify) d) Scalability requirements e) No specific requirements f) Custom performance criteria"
- **Security Level**: "What security requirements apply to this module? a) Authentication only b) Authorization and role-based access c) Data encryption at rest/transit d) Compliance requirements (specify) e) All security layers f) Custom security requirements"

### Dependencies & Integration
- **Upstream Dependencies**: "Which components/modules must be completed before this epic can start? a) Infrastructure setup b) Database schema c) Authentication system d) External API integrations e) Shared libraries f) None g) Other (specify)"
- **Downstream Impact**: "Which components/modules will depend on the outputs of this epic? a) User interface components b) Other backend services c) Analytics/reporting d) External systems e) Mobile applications f) All systems g) Other (specify)"
- **Data Dependencies**: "What data does this module need from other components? a) User/account data b) Configuration data c) Business entities d) Analytics data e) External system data f) No external data g) Other (specify)"

### Implementation Strategy
- **Development Approach**: "What implementation approach should be used? a) API-first development b) Database-first approach c) Frontend-first approach d) Test-driven development e) Domain-driven design f) Incremental/iterative builds g) Other methodology"
- **Testing Strategy**: "What testing approach is required? a) Unit tests only b) Integration testing c) End-to-end testing d) Performance testing e) Security testing f) All testing types g) Custom testing requirements"
- **Deployment Strategy**: "How should this module be deployed? a) Independent microservice b) Part of monolithic application c) Serverless functions d) Container-based deployment e) Traditional server deployment f) Hybrid approach g) Other deployment model"

### Business Context
- **Business Priority**: "What is the business priority for this epic? a) Critical path/foundational b) High priority feature c) Medium priority enhancement d) Low priority/nice-to-have e) Technical debt f) Compliance requirement"
- **User Impact**: "Who are the primary users affected by this epic? a) End users/customers b) Internal users/employees c) System administrators d) Developers/API consumers e) External partners f) All user types g) Other stakeholders"
- **Success Metrics**: "How will success be measured? a) Feature completeness b) Performance metrics c) User adoption/engagement d) System reliability e) Cost reduction f) Compliance achievement g) Custom metrics"

## Enhanced Epics Document Structure

The generated modular epics document should follow this enhanced YAML format:

```yaml
epic-{module-name}-{epic-name}:
  description: Brief description of the module-specific epic
  project_context:
    project_type: "project-type"
    technology_stack: "primary-tech-stack"
    architecture_pattern: "architecture-pattern"
  module_context:
    primary_module: module-name
    related_modules:
      - module-name-1
      - module-name-2
    technical_spec_reference: "path/to/module/specification.md"
    architecture_alignment:
      - component-1
      - component-2
    business_priority: "priority-level"

  module-initialization:
    story_id: 1
    description: Set up the foundational infrastructure and basic module structure
    goals:
      - as a developer I need to establish the module's basic structure and dependencies
      - as a system architect I should be able to verify module boundaries and contracts
      - as a DevOps engineer I need to configure module-specific deployment pipelines
    acceptance_criteria:
      - module structure follows the technical specification architecture
      - all external dependencies are properly configured and tested
      - basic health checks and monitoring are implemented
      - module can be deployed independently without affecting other modules
    dependent_stories: []
    relevant_docs:
      - "path/to/module/specification.md"
      - "path/to/architecture/overview.md"
      - "path/to/infrastructure/requirements.md"
    cross_module_dependencies:
      upstream: []
      downstream: []
    business_value: "Establishes foundation for all subsequent module development"
    risk_mitigation: "Reduces integration complexity and deployment risks"
    outputs:
      src/modules/{module-name}/config.{ext}:
        classes:
          ModuleConfig:
            attributes:
              - database_url: "str: Database connection configuration"
              - api_endpoints: "dict: External API endpoint configurations"
              - security_settings: "dict: Module-specific security configurations"
            methods:
              - load_config: >
                  def load_config(environment: str = "production") -> ModuleConfig:
                      """
                      Load module configuration based on environment
                      Validates all required settings and dependencies
                      """
      src/modules/{module-name}/models.{ext}:
        classes:
          BaseModel:
            attributes:
              - id: "UUID: Unique identifier for all module entities"
              - created_at: "datetime: Entity creation timestamp"
              - updated_at: "datetime: Last modification timestamp"
            methods:
              - validate: >
                  def validate(self) -> bool:
                      """
                      Validate model data against module specifications
                      """
      tests/test_{module-name}_initialization.{ext}:
        classes:
          TestModuleInitialization:
            methods:
              - test_config_loading: >
                  def test_config_loading():
                      """Test module configuration loading and validation"""
              - test_dependency_resolution: >
                  def test_dependency_resolution():
                      """Test external dependency connectivity and validation"""
              - test_module_health_check: >
                  def test_module_health_check():
                      """Test module health check endpoints and monitoring"""

  api-layer-implementation:
    story_id: 2
    description: Implement the module's API layer with appropriate endpoints and protocols
    goals:
      - as a client developer I need well-defined APIs to integrate with the module
      - as a backend developer I should implement secure and performant API endpoints
      - as a QA engineer I need comprehensive API documentation for testing
    acceptance_criteria:
      - all API endpoints follow project's API specification standards
      - authentication and authorization are properly implemented according to project security requirements
      - API response times meet performance requirements defined for the project
      - comprehensive error handling and validation are implemented
      - API documentation is automatically generated and up-to-date
    dependent_stories:
      - "epic-{module-name}-{epic-name}.module-initialization"
    relevant_docs:
      - "path/to/module/api-specification.md"
      - "path/to/project/security/authentication.md"
      - "path/to/project/api-standards.md"
    cross_module_dependencies:
      upstream:
        - module: "authentication-module"
          dependency: "User authentication and session management"
          interface: "Token-based authentication (specify protocol)"
      downstream:
        - module: "monitoring-module"
          dependency: "API usage metrics and logging"
          interface: "Metrics collection (specify protocol)"
    business_value: "Enables integration with other system components and external consumers"
    risk_mitigation: "Provides controlled access to module functionality with proper security"
    outputs:
      src/modules/{module-name}/api/routes.{ext}:
        classes:
          APIRouter:
            methods:
              - create_resource: >
                  @router.post("/resources")
                  async def create_resource(resource_data: ResourceCreateSchema, auth_context: AuthContext):
                      """
                      Create a new resource in the module
                      Validates input, checks permissions, and returns created resource
                      """
              - get_resource: >
                  @router.get("/resources/{resource_id}")
                  async def get_resource(resource_id: str, auth_context: AuthContext):
                      """
                      Retrieve a specific resource by ID
                      Implements proper authorization and error handling
                      """
      src/modules/{module-name}/api/schemas.{ext}:
        classes:
          ResourceCreateSchema:
            attributes:
              - name: "str: Resource name with validation rules"
              - description: "Optional[str]: Resource description"
              - configuration: "dict: Module-specific configuration data"
      tests/test_{module-name}_api.{ext}:
        classes:
          TestModuleAPI:
            methods:
              - test_create_resource_authorized: >
                  def test_create_resource_authorized():
                      """Test resource creation with valid authentication"""
              - test_api_performance: >
                  def test_api_performance():
                      """Test API response times meet project requirements"""
              - test_error_handling: >
                  def test_error_handling():
                      """Test comprehensive error handling and validation"""

  business-logic-implementation:
    story_id: 3
    description: Implement core business logic and domain-specific functionality
    goals:
      - as a business analyst I need the module to implement required business rules
      - as a developer I should have clean, testable business logic separate from API concerns
      - as a maintainer I need well-documented business logic that's easy to modify
    acceptance_criteria:
      - all business rules from module specification are implemented
      - business logic is decoupled from API and data access layers
      - comprehensive unit tests cover all business scenarios
      - business logic performance meets module requirements
      - error handling includes business-specific validation and meaningful error messages
    dependent_stories:
      - "epic-{module-name}-{epic-name}.module-initialization"
    relevant_docs:
      - "path/to/module/business-rules.md"
      - "path/to/module/specification.md"
      - "path/to/project/domain-model.md"
    cross_module_dependencies:
      upstream:
        - module: "shared-services"
          dependency: "Common business rule validation and utilities"
          interface: "Service layer calls or library imports"
      downstream:
        - module: "audit-module"
          dependency: "Business event tracking and audit trail"
          interface: "Event publishing or direct logging"
    business_value: "Implements core business functionality that delivers direct value to users"
    risk_mitigation: "Separates business logic for easier testing and maintenance"
    outputs:
      src/modules/{module-name}/services/business_logic.{ext}:
        classes:
          BusinessLogicService:
            methods:
              - process_business_operation: >
                  def process_business_operation(input_data: BusinessInput) -> BusinessResult:
                      """
                      Process module-specific business logic
                      Validates input, applies business rules, returns result
                      """
              - validate_business_rules: >
                  def validate_business_rules(data: dict) -> ValidationResult:
                      """
                      Validate data against module business constraints
                      """
      src/modules/{module-name}/domain/entities.{ext}:
        classes:
          DomainEntity:
            attributes:
              - business_attribute: "type: Business-relevant attribute description"
            methods:
              - business_method: >
                  def business_method(self, params) -> result:
                      """Domain-specific business method"""
      tests/test_{module-name}_business_logic.{ext}:
        classes:
          TestBusinessLogic:
            methods:
              - test_business_rule_processing: >
                  def test_business_rule_processing():
                      """Test core business rule implementation with various scenarios"""
              - test_edge_cases: >
                  def test_edge_cases():
                      """Test business logic edge cases and error conditions"""

  data-layer-implementation:
    story_id: 4
    description: Implement data persistence, caching, and data access patterns
    goals:
      - as a developer I need efficient data access with proper abstraction
      - as a database administrator I need optimized schemas and queries
      - as a performance engineer I need proper caching and query optimization
    acceptance_criteria:
      - data schema aligns with module data requirements and project standards
      - data access layer provides proper abstraction from storage technology
      - caching strategy is implemented for performance-critical operations
      - data migrations are properly versioned and tested
      - data integrity constraints are enforced
      - backup and recovery procedures are implemented
    dependent_stories:
      - "epic-{module-name}-{epic-name}.module-initialization"
    relevant_docs:
      - "path/to/module/data-model.md"
      - "path/to/project/database/schema-standards.md"
      - "path/to/project/data-governance.md"
    cross_module_dependencies:
      upstream:
        - module: "infrastructure"
          dependency: "Database and cache infrastructure provisioning"
          interface: "Connection pools and configuration management"
      downstream:
        - module: "analytics"
          dependency: "Data change events and ETL processes"
          interface: "Event streaming or batch data export"
    business_value: "Provides reliable and performant data storage for business operations"
    risk_mitigation: "Ensures data integrity and provides foundation for system reliability"
    outputs:
      src/modules/{module-name}/data/repository.{ext}:
        classes:
          DataRepository:
            methods:
              - create: >
                  async def create(self, entity_data: dict) -> Entity:
                      """
                      Create new entity with validation and error handling
                      """
              - find_by_criteria: >
                  async def find_by_criteria(self, criteria: dict) -> List[Entity]:
                      """
                      Find entities matching criteria with caching and pagination
                      """
              - update: >
                  async def update(self, entity_id: str, updates: dict) -> Entity:
                      """
                      Update entity with optimistic locking and validation
                      """
      src/modules/{module-name}/data/cache.{ext}:
        classes:
          CacheManager:
            methods:
              - get_cached: >
                  async def get_cached(self, key: str) -> Optional[Any]:
                      """
                      Retrieve cached data with fallback to primary storage
                      """
              - invalidate_cache: >
                  async def invalidate_cache(self, pattern: str) -> bool:
                      """
                      Invalidate cache entries matching pattern
                      """
      tests/test_{module-name}_data.{ext}:
        classes:
          TestDataLayer:
            methods:
              - test_crud_operations: >
                  def test_crud_operations():
                      """Test all CRUD operations and data integrity"""
              - test_caching_behavior: >
                  def test_caching_behavior():
                      """Test cache hit/miss scenarios and invalidation"""
              - test_data_migration: >
                  def test_data_migration():
                      """Test data migration scripts and rollback procedures"""

  integration-implementation:
    story_id: 5
    description: Implement external service integrations and cross-module communication
    goals:
      - as an integration developer I need reliable external service communication
      - as a system architect I need proper error handling and retry mechanisms
      - as a monitoring engineer I need comprehensive integration observability
    acceptance_criteria:
      - all external integrations are implemented with proper error handling
      - circuit breaker pattern is implemented for external service calls
      - integration monitoring and alerting are configured
      - retry mechanisms with exponential backoff are implemented
      - integration contracts are properly documented and tested
      - fallback mechanisms are implemented for critical integrations
    dependent_stories:
      - "epic-{module-name}-{epic-name}.business-logic-implementation"
    relevant_docs:
      - "path/to/module/integrations.md"
      - "path/to/project/integration-patterns.md"
      - "path/to/external-apis/documentation.md"
    cross_module_dependencies:
      upstream:
        - module: "infrastructure"
          dependency: "Service discovery and load balancing capabilities"
          interface: "Service mesh or API gateway configuration"
      downstream:
        - module: "monitoring"
          dependency: "Integration metrics, health checks, and alerting"
          interface: "Metrics API and health check endpoints"
    business_value: "Enables seamless integration with external systems and services"
    risk_mitigation: "Provides resilient integration patterns that handle external service failures"
    outputs:
      src/modules/{module-name}/integrations/external_client.{ext}:
        classes:
          ExternalServiceClient:
            methods:
              - call_external_service: >
                  async def call_external_service(self, endpoint: str, data: dict) -> ServiceResponse:
                      """
                      Make external service calls with retry logic and error handling
                      """
              - health_check: >
                  async def health_check(self) -> HealthStatus:
                      """
                      Check health of external service integration
                      """
      src/modules/{module-name}/integrations/circuit_breaker.{ext}:
        classes:
          CircuitBreaker:
            methods:
              - execute_with_circuit_breaker: >
                  async def execute_with_circuit_breaker(self, operation: Callable) -> Any:
                      """
                      Execute operation with circuit breaker pattern
                      """
      tests/test_{module-name}_integrations.{ext}:
        classes:
          TestIntegrations:
            methods:
              - test_external_service_integration: >
                  def test_external_service_integration():
                      """Test external service communication and error handling"""
              - test_circuit_breaker: >
                  def test_circuit_breaker():
                      """Test circuit breaker behavior under various failure conditions"""
              - test_retry_mechanisms: >
                  def test_retry_mechanisms():
                      """Test retry logic and exponential backoff"""

# Coordination Epic Template (Cross-Module Integration)
epic-integration-coordination:
  description: Coordinate cross-module integrations and shared infrastructure concerns
  project_context:
    project_type: "{project-type}"
    technology_stack: "{tech-stack}"
    architecture_pattern: "{architecture-pattern}"
  module_context:
    primary_module: "coordination"
    related_modules:
      - "all-modules"
    technical_spec_reference: "path/to/architecture/integration-patterns.md"
    architecture_alignment:
      - "integration-layer"
      - "shared-infrastructure"
      - "cross-cutting-concerns"
    business_priority: "foundational"

  cross-module-communication-system:
    story_id: 1
    description: Implement communication system for module coordination (event bus, message queue, or direct API calls)
    goals:
      - as a system architect I need reliable communication between modules
      - as a developer I need easy-to-use integration mechanisms
      - as a monitoring engineer I need visibility into cross-module communication flows
    acceptance_criteria:
      - communication system is implemented with guaranteed delivery (if required)
      - all modules can communicate using the established patterns
      - message/event schema validation is implemented
      - communication monitoring and debugging tools are available
      - error handling and dead letter processing is implemented for failed communications
    dependent_stories: []
    relevant_docs:
      - "path/to/architecture/communication-patterns.md"
      - "path/to/integration/message-schemas.md"
    cross_module_dependencies:
      upstream: []
      downstream:
        - module: "all-modules"
          dependency: "Communication capabilities for module integration"
          interface: "Communication API (REST, messaging, events)"
    business_value: "Enables scalable and reliable module communication"
    risk_mitigation: "Provides foundation for system integration and reduces coupling"
    outputs:
      src/shared/communication/communication_bus.{ext}:
        classes:
          CommunicationBus:
            methods:
              - send_message: >
                  async def send_message(self, message: Message) -> bool:
                      """
                      Send message through the communication system
                      """
              - subscribe_to_messages: >
                  def subscribe_to_messages(self, message_types: List[str], handler: MessageHandler):
                      """
                      Subscribe to specific message types with error handling
                      """
      tests/test_cross_module_communication.{ext}:
        classes:
          TestCommunicationSystem:
            methods:
              - test_message_delivery: >
                  def test_message_delivery():
                      """Test message delivery guarantees and error handling"""
```

### Enhanced Structure Rules

#### Universal Project Support
- **Project Context**: Include `project_context` section with project type, technology stack, and architecture pattern
- **Module Context**: Generic module identification and relationship mapping
- **Flexible File Extensions**: Use `{ext}` placeholder for language-specific file extensions
- **Technology Agnostic**: Structure supports various programming languages and frameworks

#### Dependency Documentation
- **Upstream Dependencies**: What this module needs from other modules/systems
- **Downstream Dependencies**: What other modules/systems need from this module
- **Interface Definitions**: Clear contracts for cross-module/system communication
- **Business Value**: Explicit business value statement for each story
- **Risk Mitigation**: Risk mitigation strategies for each story

#### Flexible Technical Specification Alignment
- **Component Mapping**: Stories map to project-specific technical components
- **Performance Requirements**: Project-specific performance criteria
- **Security Context**: Adaptable security implementations
- **Testing Strategy**: Comprehensive testing aligned with project complexity

## Documentation Analysis for Modular Epics

Before generating modular epics, analyze the project's documentation structure:

### Project-Specific Documentation
- **Technical Specifications**: Look for module/component specifications in the project
- **API Documentation**: Project-specific API standards and contracts
- **Data Models**: Project-specific data schemas and relationships
- **Integration Patterns**: Project-specific communication patterns

### Architecture Documentation
- **System Architecture**: Overall system design and module boundaries
- **Integration Specifications**: Cross-module dependency and communication documentation
- **Infrastructure Documentation**: Common infrastructure and shared service documentation
- **Communication Protocols**: Inter-module communication specifications

### Business Documentation
- **Business Requirements**: Project-specific business context and requirements
- **Functional Requirements**: Feature specifications and user stories
- **Domain Model**: Business domain concepts and rules

## Target Audience for Modular Epics

### Development Teams
- **Backend Developers**: Module-specific implementation guidance
- **Frontend Developers**: API contracts and integration patterns
- **Full-Stack Developers**: End-to-end feature implementation
- **QA Engineers**: Module-specific testing strategies and acceptance criteria

### Cross-Functional Teams
- **System Architects**: Module boundaries and integration patterns
- **DevOps Engineers**: Module-specific deployment and infrastructure requirements
- **Product Managers**: Feature delivery tracking across modules
- **Business Analysts**: Business requirement traceability

### Specialized Teams
- **Integration Engineers**: Cross-module communication and data flow
- **Performance Engineers**: Module-specific performance requirements
- **Security Engineers**: Module-specific security implementations
- **Data Engineers**: Data pipeline and analytics requirements

## Enhanced Output Requirements

### File Naming Convention
- **Module Epics**: `epic-{module-name}-{epic-name}.yaml`
- **Coordination Epics**: `epic-integration-{integration-name}.yaml`
- **Cross-Cutting Epics**: `epic-shared-{concern-name}.yaml`
- **Platform Epics**: `epic-platform-{platform-component}.yaml`

### Directory Structure Template
```
/tasks/
├── module-epics/
│   ├── epic-{module-1}-{feature}.yaml
│   ├── epic-{module-2}-{feature}.yaml
│   └── epic-{module-n}-{feature}.yaml
├── integration-epics/
│   ├── epic-integration-{integration-name}.yaml
│   └── epic-integration-{communication-system}.yaml
├── shared-epics/
│   ├── epic-shared-{shared-concern}.yaml
│   └── epic-shared-{infrastructure}.yaml
└── platform-epics/
    ├── epic-platform-{platform-component}.yaml
    └── epic-platform-{deployment}.yaml
```

## Final Enhanced Instructions

**CRITICAL - DO NOT DEVIATE FROM THESE INSTRUCTIONS:**

1. **DO NOT** start implementing the epics document immediately
2. **ALWAYS** ask project-specific and module-specific clarifying questions before generating the document
3. **MUST** analyze project's technical documentation structure first to understand project context
4. **MUST** follow the enhanced YAML format structure with project and module context
5. **MUST** include cross_module_dependencies for each story with project-specific details
6. **MUST** reference project-specific technical documentation in relevant_docs
7. **MUST** align stories with project-specific technical components and architecture
8. **MUST** include comprehensive test coverage appropriate for the project's testing standards
9. **MUST** document integration interfaces for cross-module communication using project patterns
10. **MUST** validate that dependencies reference valid modules and interfaces within the project
11. **MUST** include business_value and risk_mitigation for each story
12. **DO NOT** generate implementation code - only the modular epics document
13. **DO NOT** modify existing files - only create the new modular epics YAML file
14. **MUST** adapt file extensions ({ext}) to match the project's primary programming language

### Universal Requirements
- **Project Adaptation**: Stories must adapt to the specific project's technology stack and architecture
- **Business Context**: Include business value and priority appropriate to the project domain
- **Technical Flexibility**: Support various architectural patterns (monolithic, microservices, serverless, etc.)
- **Integration Patterns**: Adapt integration approaches to project's communication patterns
- **Testing Standards**: Align testing requirements with project's quality standards

### Cross-Project Compatibility
- **Language Agnostic**: Support multiple programming languages and frameworks
- **Domain Flexible**: Work across different business domains and project types
- **Scale Adaptive**: Support projects of various sizes and complexity levels
- **Pattern Flexible**: Support different architectural and design patterns
- **Team Structure**: Adapt to different team sizes and organizational structures

**WARNING:** Deviating from these enhanced instructions or the specified universal format will result in epics that don't align with the project's specific requirements. Stay focused on creating project-appropriate, module-specific epics that implement the project's technical specifications while maintaining clear cross-module integration patterns adapted to the project's context.
