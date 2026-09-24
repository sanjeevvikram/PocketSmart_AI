# Phase 5 – Project Development

## 1. Project Development Overview

The Project Development phase focuses on implementing the PocketSmart AI system based on the requirements, design, and planning completed in the previous phases.

The application is developed as a web-based AI-assisted budgeting and recommendation system using FastAPI, SQLite, HTML, CSS, JavaScript, and the Gemini AI service.

The development process follows a modular approach so that authentication, database operations, AI services, product recommendations, planning logic, and frontend functionality can be developed and tested independently.

---

## 2. Development Environment

The following tools and technologies are used for development:

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Database | SQLite |
| ORM / Database Layer | SQLAlchemy |
| Data Validation | Pydantic |
| AI Service | Google Gemini API |
| AI Model | Gemini 3.6 Flash |
| Frontend | HTML, CSS, JavaScript |
| Development Environment | Visual Studio Code |
| API Testing | FastAPI Swagger / Pytest |
| Version Control | Git |
| Repository | GitHub |

The development environment is configured using a Python virtual environment.

Sensitive configuration values such as API keys and secret keys are stored in environment variables.

---

## 3. Project Structure

The main project structure is organized as follows:

```text
PocketSmart_AI/
│
├── app/
│   ├── models/
│   │   ├── db.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   │
│   ├── routes/
│   │   ├── api.py
│   │   ├── pages.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── catalog.py
│   │   ├── gemini_utils.py
│   │   └── __init__.py
│   │
│   ├── static/
│   ├── templates/
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   └── __init__.py
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── pytest.ini
├── README.md
└── requirements.txt
4. Backend Development

The backend is developed using FastAPI.

The backend is responsible for:

Handling HTTP requests
User authentication
User registration
User login
Session management
Database operations
Shopping-plan generation
Budget calculations
Product recommendations
Gemini AI integration
Error handling
API responses

FastAPI also provides automatically generated API documentation that can be used during development and testing.

5. Database Development

SQLite is used as the database for the project.

The database layer manages persistent application data such as user information and application records.

The database implementation includes:

Database connection configuration
SQLAlchemy models
Database initialization
User data storage
Database session management
Data validation

Database initialization is performed when the application starts so that required tables are available before requests are processed.

6. Authentication Development

Authentication functionality is implemented to provide secure access to user-specific features.

The authentication system includes:

User registration
User login
Password validation
Password hashing
Authentication token/session handling
Session information
Protected API access
Logout/session termination where applicable

User credentials are not stored as plain-text passwords.

Authentication-related secrets are stored through environment configuration rather than hard-coded in source code.

7. AI Integration Development

Gemini AI is integrated into PocketSmart AI to provide intelligent planning and recommendation functionality.

The AI service is implemented separately in the services layer.

The AI integration performs tasks such as:

Processing planning requirements
Understanding user preferences
Generating recommendations
Supporting budget-based planning
Producing summaries
Improving recommendation quality

The Gemini API key is loaded from environment variables.

The configured Gemini model is used through the Google GenAI Python SDK.

8. AI Fallback Mechanism

A fallback mechanism is included to improve application reliability when the external AI service is unavailable or an AI request fails.

If the Gemini service cannot generate a response, the application can use predefined application logic and catalog information to produce a fallback result.

The fallback mechanism helps prevent complete application failure due to:

API errors
Network problems
Invalid AI responses
Service unavailability
Temporary API limitations

This allows the core application functionality to remain usable even when the AI service is temporarily unavailable.

9. Product Catalog Development

A product catalog service is implemented to support recommendation and shopping-plan generation.

The catalog service provides product information that can be used by the planning logic.

Catalog information may include:

Product name
Product category
Product type
Approximate price
Product description
Shopping/search information

The catalog service is kept separate from the main API routes so that product-related logic can be maintained independently.

10. Budget Planning Development

The budget planning functionality processes the user's available budget and selected requirements.

The planning logic considers:

Planner
Budget
Estimated Total
Budget Remaining
Category Allocation
Summary
Recommendations
AI Generated Status
Source Information

11. API Development

The backend exposes API endpoints for application functionality.

The API layer handles operations related to:

Authentication
Session information
Planning requests
Recommendations
Product information
Application data

The API follows a structured request and response format.

Pydantic schemas are used where appropriate to validate request data and structure API responses.

12. Frontend Development

The frontend provides the user interface for interacting with PocketSmart AI.

The frontend uses:

HTML
CSS
JavaScript
FastAPI templates/static files

The interface is designed to allow users to:

Open the application.
Register an account.
Log in.
Enter planning requirements.
Provide budget information.
Request recommendations.
View generated results.
Review estimated costs.
Use the available shopping/product information.

Frontend pages communicate with the backend APIs to retrieve and display application data.

13. Error Handling Development

Error handling is implemented throughout the application.

The system handles common situations such as:

Invalid input
Missing required fields
Incorrect login credentials
Duplicate user registration
Database errors
AI API failures
Invalid AI responses
Unavailable services

Meaningful HTTP status codes and error messages are returned where appropriate.

This improves reliability and makes debugging easier during development and testing.

14. Configuration Management

APP_NAME
ENVIRONMENT
SECRET_KEY
DATABASE_URL
GEMINI_API_KEY
GEMINI_MODEL
FRONTEND_ORIGINS
MAX_IMAGE_MB

15. Security Development

Security considerations are included during implementation.

The main security practices include:

Password hashing
Environment-based secret management
API key protection
Input validation
Authentication checks
Protected application functionality
Secure handling of user data
.env exclusion from Git
Database access through the application data layer

Sensitive credentials are not intentionally included in the public GitHub repository.

16. Testing During Development

Testing is performed continuously during implementation.

The development process includes:

Unit testing
API testing
Authentication testing
Database testing
AI service testing
Fallback testing
Manual browser testing
Frontend/API integration testing

Automated tests are maintained in the tests/ directory.

Pytest is used to execute the automated test suite.

17. Version Control During Development

Implement Feature
       |
       v
Run Tests
       |
       v
Fix Errors
       |
       v
Git Add
       |
       v
Git Commit
       |
       v
Git Push
       |
       v
GitHub Repository

18. Development Milestones

The main development milestones are:

Milestone 1 – Environment Setup
Configure Python environment
Install dependencies
Configure project structure
Configure environment variables
Milestone 2 – Database and Authentication
Implement database connection
Create database models
Implement registration
Implement login
Implement authentication handling
Milestone 3 – Backend API
Implement FastAPI routes
Implement request validation
Implement response handling
Implement planning logic
Milestone 4 – AI Integration
Configure Gemini API
Implement AI service
Generate AI-assisted recommendations
Implement fallback behavior
Milestone 5 – Product and Planning Integration
Implement catalog service
Connect product information with planning logic
Calculate estimated costs
Calculate remaining budget
Milestone 6 – Frontend Integration
Implement application pages
Connect frontend with APIs
Display planning results
Improve user interaction
Milestone 7 – Testing and Optimization
Run automated tests
Test APIs
Test authentication
Test AI integration
Fix errors
Improve reliability
Milestone 8 – Final Preparation
Complete documentation
Organize GitHub repository
Prepare project demonstration
Verify final application workflow
19. Current Development Status

The PocketSmart AI application has been developed using the planned technology stack.

The current implementation includes:

FastAPI backend
SQLite database
User authentication
API routes
Product catalog service
Budget planning functionality
Gemini AI integration
AI fallback handling
Frontend pages
Automated testing
Git version control
GitHub repository

The development phase continues with verification, refinement, testing, and preparation for final documentation and demonstration.

20. Development Completion Criteria

The development phase is considered ready for the testing phase when:

Core backend functionality is implemented.
Database functionality is working.
Authentication functionality is working.
Planning functionality is implemented.
Product catalog functionality is available.
Gemini AI integration is configured.
AI fallback handling is available.
Frontend and backend are connected.
Application errors are handled.
Automated tests are available.
Project files are organized.
Source code is maintained in GitHub.
21. Conclusion

The Project Development phase converts the planned PocketSmart AI design into a working software application.

The implementation covers the backend, database, authentication, AI integration, product catalog, budget planning, frontend, error handling, security, testing, and version control.

The completed development work provides the foundation for the next phase, which focuses on systematic testing and verification of the application.