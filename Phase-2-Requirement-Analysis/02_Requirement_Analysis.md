# Phase 2 – Requirement Analysis

## 1. Functional Requirements

The system shall provide the following functions:

### 1.1 User Registration
- The user shall be able to create an account using an email and password.
- The system shall prevent duplicate email registration.

### 1.2 User Login
- The user shall be able to log in using registered credentials.
- The system shall validate the user's credentials.
- The system shall maintain the user's authenticated session.

### 1.3 Budget Planning
- The user shall be able to enter a shopping budget.
- The system shall calculate estimated spending.
- The system shall calculate the remaining budget.
- The system shall provide category-wise budget allocation.

### 1.4 User Preferences
The system shall accept preferences such as:
- Shopping category
- Budget
- Style
- Required items
- Other user requirements

### 1.5 AI Recommendations
- The system shall process the user's requirements using an AI service.
- The system shall generate personalized recommendations.
- The recommendations shall be returned in a structured format.

### 1.6 Fallback Recommendations
- If the AI service is unavailable, the system shall provide catalog-based recommendations.
- The application shall remain usable even when AI generation fails.

### 1.7 Product Categories
The system shall support categories such as:
- Home
- Party
- Jewelry

The application shall allow additional categories to be added in the future.

### 1.8 API
The system shall provide backend API endpoints for:
- Authentication
- User sessions
- Budget planning
- AI recommendations
- Application data

---

## 2. Non-Functional Requirements

### 2.1 Performance
- The application should respond to normal user requests within a reasonable time.
- AI requests should handle temporary service failures gracefully.

### 2.2 Reliability
- The system shall provide fallback recommendations when AI generation is unavailable.
- Application errors shall not expose sensitive information.

### 2.3 Security
- User passwords shall not be stored as plain text.
- Authentication shall use secure session/token mechanisms.
- API credentials shall be stored using environment variables.
- Sensitive configuration files such as `.env` shall not be committed to GitHub.

### 2.4 Usability
- The application shall provide a simple user interface.
- Users should be able to enter their requirements easily.
- Results should be presented in an understandable format.

### 2.5 Maintainability
- The application shall use a modular project structure.
- Backend routes, services, models, and configuration shall be separated.
- The source code shall be maintained using Git and GitHub.

---

## 3. User Requirements

The user should be able to:

1. Register an account.
2. Log in to the application.
3. Enter a shopping budget.
4. Select a shopping category.
5. Specify preferences.
6. Enter required items.
7. Request recommendations.
8. View estimated spending.
9. View remaining budget.
10. View AI-generated or fallback recommendations.

---

## 4. System Requirements

The system requires:

- Python 3.12 or compatible Python version
- FastAPI
- Uvicorn
- SQLite
- Google Gemini API
- HTML
- CSS
- JavaScript
- Git
- GitHub
- Modern web browser

---

## 5. Hardware / Software Requirements

### Hardware Requirements

Minimum recommended configuration:

- Processor: Dual-core processor
- RAM: 4 GB or more
- Storage: At least 1 GB available
- Internet connection for AI functionality

### Software Requirements

- Windows, Linux, or macOS
- Python 3.12
- Visual Studio Code or another Python-compatible IDE
- Modern web browser
- Git
- Internet connection

---

## 6. Technology Requirements

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- SQLite
- SQLAlchemy

### Artificial Intelligence
- Google Gemini API
- Google GenAI Python SDK

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Pytest

---

## 7. Input Requirements

The application may accept the following inputs:

| Input | Description |
|---|---|
| Email | User's registered email |
| Password | User authentication password |
| Budget | Maximum amount the user wants to spend |
| Category | Shopping category |
| Style | Preferred style |
| Items | Items required by the user |
| Preferences | Additional shopping requirements |

Example:

```text
Budget: ₹10,000
Category: Home
Style: Modern
Items: Sofa, Lamp, Wall Decor
## 8. Output Requirements

The system should provide the following outputs:

| Output | Description |
|---|---|
| Budget Plan | Displays the planned spending based on the user's budget |
| Recommended Items | Provides suitable products based on user requirements |
| Category Allocation | Shows the suggested amount for different categories |
| Estimated Total | Displays the estimated total cost of selected items |
| Remaining Budget | Shows the amount remaining after estimated spending |
| AI Recommendations | Provides AI-generated shopping suggestions |
| Shopping Links | Provides links or references for suggested products |
| Summary | Displays a simple summary of the generated shopping plan |

Example:

```text
Budget: ₹10,000
Category: Home
Style: Modern

Recommended Items:
1. Sofa
2. Table Lamp
3. Wall Decor

Estimated Total: ₹8,500
Remaining Budget: ₹1,500

The application should work through a web browser.
Users must register and log in before using personalized features.
The system should respect the budget provided by the user.
AI-generated recommendations depend on the availability of the configured AI service.
Product prices and availability may change over time.
The project is intended as a prototype/academic project.
The application should not expose sensitive user information.
API keys and secret configuration values should be stored securely.
The system should provide fallback recommendations when AI services are unavailable.
The application should be easy to use for users with basic computer knowledge.
10. Expected System Behavior

The expected behavior of the system is:

The user opens the PocketSmart AI application.
The user creates an account or logs in.
The user enters a shopping budget.
The user selects a shopping category.
The user provides preferred style and required items.
The system validates the user input.
The system processes the shopping requirements.
The AI service generates suitable recommendations when available.
The system calculates the estimated spending.
The system displays the recommended shopping plan.
The system displays the estimated total and remaining budget.
If the AI service is unavailable, the system provides fallback recommendations.
The user can review the generated plan and make purchasing decisions.
11. Security Requirements

The application should follow basic security practices:

User passwords should not be stored as plain text.
Authentication should be required for protected features.
API keys should be stored in environment variables.
Sensitive configuration files such as .env should not be committed to GitHub.
User input should be validated before processing.
Authentication tokens should be handled securely.
Database access should be controlled by the application.
12. Performance Requirements

The system should:

Respond to normal user requests within a reasonable time.
Avoid unnecessary API requests.
Handle temporary AI service failures gracefully.
Provide fallback results when the AI service is unavailable.
Maintain stable operation during normal project usage.
13. Usability Requirements

The application should:

Provide a simple and understandable interface.
Use clear labels and instructions.
Display budget information clearly.
Show recommendations in an easy-to-read format.
Provide meaningful error messages.
Allow users to easily understand the generated shopping plan.

## 14. Acceptance Criteria

The project will be considered functional when:

- A user can register successfully.
- A registered user can log in.
- A user can enter a shopping budget.
- A user can select a category and style.
- A user can enter required items.
- The system can generate a shopping plan.
- The system calculates estimated spending.
- The system displays the remaining budget.
- AI recommendations work when the AI service is available.
- Fallback recommendations work when the AI service is unavailable.
- The application passes the project tests.

## 15. Conclusion

The Requirement Analysis phase defines the functional, technical, security, performance, and usability requirements of PocketSmart AI.

These requirements provide the foundation for the next phase, Project Design, where the system architecture, database design, user interface design, and application workflow will be defined.