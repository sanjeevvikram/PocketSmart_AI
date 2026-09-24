# Phase 3 – Project Design

## 1. System Architecture

PocketSmart AI follows a modular web application architecture. The system is designed to allow users to register, log in, enter shopping requirements, define a budget, and receive a budget-aware shopping plan.

The main architecture consists of the following layers:

1. Presentation Layer
2. Application/API Layer
3. Business Logic Layer
4. AI Integration Layer
5. Data Access Layer
6. Database Layer

### 1.1 High-Level Architecture

```text
User
  |
  v
Web Browser
  |
  v
FastAPI Application
  |
  +----------------------+
  |                      |
  v                      v
Web Pages             REST API
  |                      |
  +----------+-----------+
             |
             v
      Business Logic
             |
      +------+------+
      |             |
      v             v
  AI Service    Catalog Service
      |             |
      v             v
 Gemini API    Product Data
      |
      v
 AI Recommendations
             |
             v
        Database

## 2. Technology Architecture

PocketSmart AI uses a lightweight web-based architecture designed for simplicity, maintainability, and future expansion.

### 2.1 Frontend

The frontend provides the user interface for interacting with the application.

Main responsibilities:

- User registration
- User login
- Budget input
- Category selection
- Style selection
- Required item input
- Shopping plan display
- AI recommendation display
- Remaining budget display

The frontend communicates with the backend through HTTP requests and REST APIs.

### 2.2 Backend

The backend is implemented using FastAPI.

Main responsibilities:

- Handle user authentication
- Validate user input
- Manage application logic
- Generate shopping plans
- Calculate estimated spending
- Communicate with the Gemini AI service
- Provide fallback recommendations
- Return results to the frontend

### 2.3 Database

SQLite is used as the initial database.

The database stores application information such as:

- User accounts
- Authentication information
- User preferences
- Shopping plans
- Generated recommendations

The database can be migrated to PostgreSQL or another production database in the future.

### 2.4 AI Service

Google Gemini is used as the AI recommendation service.

The AI service receives structured shopping requirements and generates recommendations based on:

- Budget
- Category
- Style
- Required items
- User preferences

If the Gemini service is unavailable, the application uses predefined catalog-based fallback recommendations.

---

## 3. Application Workflow

The application follows the workflow below:

1. User opens PocketSmart AI.
2. User creates an account or logs into an existing account.
3. User enters the maximum shopping budget.
4. User selects a shopping category.
5. User selects a preferred style.
6. User enters required items.
7. User submits the shopping requirements.
8. The backend validates the submitted information.
9. The application sends the requirements to the recommendation service.
10. Gemini generates AI-based recommendations when available.
11. The catalog service provides product information.
12. The application estimates the total spending.
13. The remaining budget is calculated.
14. The shopping plan is returned to the user.
15. The user can review the recommendations and shopping links.

---

## 4. System Components

### 4.1 Authentication Component

The authentication component manages user registration and login.

Responsibilities:

- Register new users
- Validate email addresses
- Securely hash passwords
- Authenticate existing users
- Create authenticated sessions/tokens
- Protect authenticated API operations

### 4.2 Shopping Planner Component

The shopping planner processes the user's shopping requirements.

Inputs include:

- Budget
- Category
- Style
- Required items
- Preferences

The planner produces:

- Recommended items
- Estimated prices
- Estimated total
- Remaining budget
- Shopping links
- Summary

### 4.3 Catalog Component

The catalog component provides predefined product information for the application.

It contains category-specific product data for areas such as:

- Home
- Party
- Jewelry

The catalog also provides fallback recommendations when the AI service is unavailable.

### 4.4 AI Recommendation Component

The AI recommendation component communicates with Google Gemini.

Its responsibilities include:

- Preparing the user requirements
- Sending prompts to Gemini
- Receiving AI-generated recommendations
- Processing the AI response
- Returning structured recommendations

### 4.5 Budget Calculation Component

The budget component calculates the estimated spending.

Formula:

```text
Remaining Budget = User Budget - Estimated Total

## 5. Database Design

PocketSmart AI uses SQLite as the initial database because it is lightweight, simple to configure, and suitable for local development.

### 5.1 Main Database Entities

The application uses the following main entities:

| Entity | Purpose |
|---|---|
| User | Stores registered user accounts |
| Shopping Plan | Stores user shopping plans |
| Recommendation | Stores generated recommendations |
| Shopping Item | Stores items included in a shopping plan |

### 5.2 User Data

The User entity contains:

- User ID
- Email
- Password hash
- Account creation date

Passwords are never stored as plain text. The application stores a secure password hash.

### 5.3 Shopping Plan Data

A shopping plan contains:

- Plan ID
- User ID
- Budget
- Category
- Style
- Requested items
- Preferences
- Estimated total
- Remaining budget
- Creation date

### 5.4 Recommendation Data

Recommendations may contain:

- Product or item name
- Category
- Estimated price
- Reason for recommendation
- Shopping link
- Recommendation source

---

## 6. API Design

PocketSmart AI provides REST API endpoints using FastAPI.

### 6.1 Authentication APIs

The authentication module provides endpoints for:

- User registration
- User login
- Current session information
- User logout

Example endpoints:

```text
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/session-info
POST /api/auth/logout

## 6.2 Planning API

The planning API is responsible for creating a shopping plan based on the user's requirements.

The user provides:

- Budget
- Category
- Style
- Required items
- Additional preferences

The backend validates the information and sends it to the business logic layer.

Example endpoint:

```text
POST /api/plan

{
  "budget": 10000,
  "category": "Home",
  "style": "Modern",
  "items": [
    "Sofa",
    "Table Lamp",
    "Wall Decor"
  ],
  "preferences": "Simple and modern"
}
The API returns:

- Recommended items
- Estimated prices
- Estimated total
- Remaining budget
- AI recommendations
- Shopping links

## 6.3 Health Check API

The health check endpoint is used to verify that the PocketSmart AI backend is running correctly.

Example endpoint:

```text
GET /api/health

{
  "planner": "home",
  "budget": 10000,
  "estimated_total": 8500,
  "budget_remaining": 1500,
  "recommendations": [],
  "summary": "Recommended home products within the specified budget."
}

### 6.4 API Error Handling

The API layer returns clear responses when a request cannot be processed successfully.

Common error cases include:

- Invalid or missing input data.
- Incorrect user credentials.
- Unauthorized access to protected endpoints.
- Duplicate user registration.
- AI service unavailable.
- Invalid shopping plan parameters.
- Internal server errors.

Example error response:

```text
{
    "detail": "Invalid request data."
}

The backend uses appropriate HTTP status codes to communicate the result of each request.

| Status Code | Meaning |
|---|---|
| 200 | Request completed successfully |
| 201 | Resource created successfully |
| 400 | Invalid request |
| 401 | Authentication required |
| 404 | Resource not found |
| 409 | Resource already exists |
| 422 | Validation error |
| 500 | Internal server error |

This approach provides predictable API behavior and makes it easier for the frontend to display meaningful messages to users.
### 6.5 Security Considerations

The PocketSmart AI application applies basic security practices to protect user data and API access.

Security measures include:

- Passwords are stored using secure password hashing.
- Authentication is handled using signed tokens.
- Protected API endpoints require authentication.
- Sensitive configuration values are stored in environment variables.
- API keys and secrets are not stored directly in the source code.
- Input data is validated before processing.
- Database queries are handled through the application data layer.
- CORS configuration controls allowed frontend origins.

These measures provide a basic security foundation for the application and can be strengthened further before production deployment.

### 6.6 API Request and Response Flow

The API follows a simple request and response flow between the frontend and backend.

1. The user enters the required information through the frontend.
2. The frontend sends the information to the appropriate API endpoint.
3. The backend validates the request data.
4. The business logic processes the request.
5. The catalog service provides product information when required.
6. The AI service generates recommendations when the AI service is available.
7. The backend calculates the estimated spending and remaining budget.
8. The backend returns the generated shopping plan to the frontend.
9. The frontend displays the result to the user.

The API design keeps the frontend and backend responsibilities separated and allows each component to be developed and tested independently.

### 6.7 API Testing

The API endpoints are tested to verify that the backend behaves correctly for valid and invalid requests.

Testing covers:

- User registration.
- User login.
- Session information.
- User logout.
- Shopping plan generation.
- Health check.
- Invalid request validation.
- Unauthorized API access.
- Duplicate user registration.
- AI service fallback behavior.

The automated test suite verifies the main application workflows and helps identify errors before deployment.

Successful API testing confirms that the backend endpoints, authentication flow, validation logic, business logic, and fallback mechanisms work together correctly.

## 10. Data Flow

The PocketSmart AI application follows a structured data flow between the user interface, backend API, business logic, AI service, catalog service, and database.

### 10.1 User Request Flow

The general request flow is:

1. The user enters planning requirements through the frontend.
2. The frontend sends the request to the FastAPI backend.
3. The API validates the submitted information.
4. The business logic processes the request.
5. The catalog service provides relevant product data.
6. The AI service generates recommendations when AI processing is required.
7. The backend combines the generated recommendations with product information.
8. The final response is returned to the frontend.
9. The frontend displays the recommendations and budget information to the user.

### 10.2 Authentication Data Flow

The authentication flow works as follows:

1. A new user submits registration information.
2. The backend validates the email and password.
3. The password is securely hashed before being stored.
4. The user can log in using the registered credentials.
5. The backend verifies the password.
6. A signed authentication token is created.
7. The token is used to access protected API endpoints.
8. The user can log out to terminate the current session.

### 10.3 AI Planning Data Flow

For an AI-powered shopping plan:

```text
User Requirements
       |
       v
Frontend
       |
       v
FastAPI API
       |
       v
Input Validation
       |
       v
Business Logic
       |
       +------------------+
       |                  |
       v                  v
Catalog Service       AI Service
       |                  |
       |             Gemini API
       |                  |
       +--------+---------+
                |
                v
       Recommendation Plan
                |
                v
             Database
                |
                v
            Frontend

Budget information is processed throughout the planning workflow.

The system receives the user's budget and selected requirements, calculates the estimated cost of recommended products, and determines the remaining budget.

The response can include:

Total budget
Estimated total cost
Remaining budget
Product recommendations
Category allocations
Planning summary

This allows the frontend to present the shopping plan in a clear and structured format.

User Input
    |
    v
API Request
    |
    v
Schema Validation
    |
    +---- Invalid ----> Error Response
    |
    v
Business Logic
    |
    v
AI / Catalog Processing
    |
    v
Validated Response

{
  "detail": "Invalid request data."
}


User
 |
 v
Frontend
 |
 v
FastAPI Backend
 |
 +------> Authentication ------> Database
 |
 +------> Business Logic
 |              |
 |              +------> Catalog Service
 |              |
 |              +------> Gemini AI Service
 |                             |
 |                             v
 |                        AI Recommendations
 |
 v
Final Shopping Plan
 |
 v
Frontend
 |
 v
User

## 9. Security Design

### 9.1 Authentication Security

PocketSmart AI uses authentication to protect user accounts and private application features.

Security measures include:

- User passwords are securely hashed before being stored.
- Authentication tokens are signed using a server-side secret.
- Protected API endpoints require valid authentication.
- User sessions are validated before accessing protected resources.
- Authentication credentials are never stored in plain text.

### 9.2 API Security

The API layer applies the following security controls:

- Request data is validated before processing.
- Protected endpoints require authentication.
- Invalid requests return appropriate HTTP status codes.
- Duplicate registrations are rejected.
- Sensitive configuration values are loaded from environment variables.
- API keys are not stored directly in source code.
- CORS is configured to allow only approved frontend origins.

### 9.3 Database Security

The application protects database information by:

- Using the application data layer for database operations.
- Validating user input before database operations.
- Storing password hashes instead of plain-text passwords.
- Preventing direct exposure of database credentials.
- Keeping local database files outside source-control commits.

### 9.4 Gemini API Security

The Gemini API key is stored in the environment configuration.

```text
Application
    |
    v
Environment Variables
    |
    v
Gemini API Key
    |
    v
Gemini Service
    |
    v
Gemini API

## 10. Data Flow

### 10.1 Overall Application Data Flow

The overall data flow of PocketSmart AI is:

```text
User
  |
  v
Frontend / Web Interface
  |
  v
FastAPI API Layer
  |
  v
Request Validation
  |
  +-------------------+
  |                   |
  v                   v
Authentication     Planning Request
  |                   |
  v                   v
User Database      Business Logic
                      |
              +-------+-------+
              |               |
              v               v
        AI Service       Catalog Service
              |               |
              v               v
         Gemini API       Product Data
              |               |
              +-------+-------+
                      |
                      v
              Recommendation
                      |
                      v
                   Database
                      |
                      v
                 API Response
                      |
                      v
                  Frontend
                      |
                      v
                     User
Registration
    |
    v
Validate User Data
    |
    v
Hash Password
    |
    v
Store User
    |
    v
Login
    |
    v
Verify Credentials
    |
    v
Create Authentication Token
    |
    v
Authenticated Session

User Input
    |
    v
Budget + Category + Style + Items
    |
    v
API Validation
    |
    v
Planning Service
    |
    +------------------+
    |                  |
    v                  v
Catalog Service    Gemini AI Service
    |                  |
    v                  v
Product Data       AI Analysis
    |                  |
    +--------+---------+
             |
             v
      Final Recommendations
             |
             v
       Budget Calculation
             |
             v
        API Response
             |
             v
          Frontend
User Request
     |
     v
Request Validation
     |
     +---- Invalid ----> 400 / 422 Response
     |
     v
Authentication
     |
     +---- Unauthorized ----> 401 Response
     |
     v
Business Logic
     |
     +---- Duplicate ----> 409 Response
     |
     v
AI / Database Services
     |
     +---- Failure ----> 500 Response
     |
     v
Successful Response
