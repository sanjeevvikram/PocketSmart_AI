# Phase 8 – Project Demonstration

## 1. Project Demonstration Overview

The Project Demonstration phase is the final phase of the PocketSmart AI project.

The purpose of this phase is to demonstrate the completed application, explain its purpose and benefits, show the working process, and present the final output.

The demonstration will show the application from the user's perspective and explain the major technical components implemented during the project.

---

## 2. Demonstration Objectives

The main objectives of the project demonstration are:

1. Introduce the PocketSmart AI project.
2. Explain the problem addressed by the project.
3. Explain the proposed solution.
4. Present the major features.
5. Demonstrate the application workflow.
6. Show user registration and login.
7. Demonstrate budget planning.
8. Demonstrate recommendations.
9. Show Gemini AI integration.
10. Show the generated planning result.
11. Explain the benefits of the application.
12. Present the final project output.
13. Demonstrate the completed project repository and documentation.

---

## 3. Project Name

### PocketSmart AI

**PocketSmart AI – Your Smart Budget & Recommendation Assistant**

PocketSmart AI is an AI-assisted budgeting and recommendation web application designed to help users make budget-aware planning decisions.

---

## 4. Project Purpose

The main purpose of PocketSmart AI is to help users plan their spending based on a defined budget and requirements.

The application combines:

- Budget planning
- Product information
- Recommendation logic
- Gemini AI assistance
- User authentication
- Web-based interaction

The system provides structured recommendations and estimated budget information to help users understand possible spending options.

---

## 5. Problem Addressed

Users may find it difficult to plan purchases when they have a limited budget and multiple requirements.

Common difficulties include:

- Comparing different options
- Estimating total costs
- Staying within a fixed budget
- Selecting suitable products
- Organizing requirements
- Finding recommendations efficiently

PocketSmart AI provides a centralized application to assist with these planning activities.

---

## 6. Proposed Solution

PocketSmart AI accepts user requirements and budget information and processes them using application planning logic, product catalog information, and Gemini AI assistance.

The system generates a structured planning result that may include:

- Planner category
- Available budget
- Estimated total
- Remaining budget
- Category allocation
- Summary
- Recommendations
- AI-generated status
- Product or shopping information

If the external AI service is unavailable, fallback logic can provide an alternative result.

---

## 7. Major Features

The major features demonstrated in the project are:

### User Registration

Users can create an account using the registration functionality.

### User Login

Registered users can log in using their credentials.

### Session Management

The application can determine the user's authentication/session status.

### Budget Planning

Users can enter their available budget and planning requirements.

### AI-Assisted Recommendations

Gemini AI can be used to generate intelligent planning and recommendation results.

### Product Catalog

The application provides product-related information to support planning.

### Budget Calculation

The application calculates estimated costs and remaining budget.

### Fallback Processing

The application can use fallback logic when the external AI service is unavailable.

---

## 8. Demonstration Environment

The project demonstration can be performed using the following environment:

| Component | Technology |
|---|---|
| Operating System | Windows |
| Programming Language | Python |
| Backend | FastAPI |
| Database | SQLite |
| AI Service | Google Gemini API |
| AI Model | Gemini 3.6 Flash |
| Frontend | HTML, CSS, JavaScript |
| Testing | Pytest |
| Development Environment | Visual Studio Code |
| Version Control | Git |
| Repository | GitHub |
| Browser | Modern Web Browser |

---

## 9. Application Startup

The demonstration begins by starting the FastAPI application.

The application can be started using:

```text
uvicorn app.main:app

10. Home Page Demonstration

The home page is shown first.

The presenter explains:

Project name
Purpose of the application
Main functionality
User workflow
AI-assisted planning concept

The home page provides the starting point for interacting with PocketSmart AI.

11. User Registration Demonstration

The registration functionality is demonstrated by creating a test user account.

The presenter shows:

Opening the registration page.
Entering an email address.
Entering a password.
Submitting the registration form.
Showing the registration response.

The demonstration should use a test account rather than real personal credentials.

12. User Login Demonstration

After registration, the presenter demonstrates login.

The steps are:

Open the login page.
Enter the test email.
Enter the test password.
Submit the login form.
Verify successful authentication.
Continue to the application functionality.

This demonstrates the authentication workflow.

13. Planning Input Demonstration

The presenter enters the information required to create a planning request.

Example information may include:

Planning Category: Home
Budget: ₹10,000
Style: Modern
Requirements: Selected items

The values used during the demonstration can be changed depending on the scenario.

The presenter explains how the input affects the generated planning result.

14. Budget Planning Demonstration

The presenter submits the planning request with the selected budget.

The application processes the request and calculates information such as:

Available budget
Estimated total
Budget remaining
Category allocation
Recommended items

The presenter explains how the result helps users understand their potential spending.

15. Gemini AI Demonstration

The presenter explains the role of Gemini AI in PocketSmart AI.

User Requirements
       |
       v
Planning Request
       |
       v
FastAPI Backend
       |
       v
Gemini AI Service
       |
       v
AI Response
       |
       v
Processed Recommendation
       |
       v
User Interface

16. Recommendation Result Demonstration

The generated recommendation result is displayed to the user.

The presenter explains important result fields such as:

Planner
Budget
Estimated Total
Budget Remaining
Category Allocation
Summary
Recommendations
AI Generated Status

The presenter explains how these values help the user understand the generated plan.

17. Product Catalog Demonstration

The product/catalog functionality is demonstrated where applicable.

The presenter explains how product information can support the planning process.

The displayed information may include:

Product name
Category
Approximate price
Description
Shopping/search information

Product prices or shopping information should be treated as illustrative unless verified against a live platform.

18. AI Fallback Demonstration

The project includes fallback behavior for situations where the Gemini service cannot provide a valid response.

The presenter explains that possible causes include:

API failure
Network problem
Temporary service unavailability
Invalid AI response

Instead of completely failing, the application can use predefined application logic and catalog information to generate a fallback result.

The fallback functionality demonstrates the reliability design of the project.

19. Error Handling Demonstration

The presenter can demonstrate basic error handling using safe test inputs.

Examples include:

Invalid login credentials
Duplicate registration
Missing required input
Invalid budget value
Invalid API request

The presenter explains that validation and error handling help prevent unexpected application failures.

20. API Documentation Demonstration

The FastAPI Swagger interface can be demonstrated through:

/docs

when the application is running.

The presenter can show:

Available API endpoints
Request parameters
Request body
Response format
HTTP status codes

pytest

3 passed

Phase 1 – Brainstorming and Ideation
Phase 2 – Requirement Analysis
Phase 3 – Project Design
Phase 4 – Project Planning
Phase 5 – Project Development
Phase 6 – Project Testing
Phase 7 – Project Documentation
Phase 8 – Project Demonstration

25. Final Output

The final output of PocketSmart AI is a working web application that can:

Authenticate users.
Accept planning requirements.
Process budget information.
Generate recommendations.
Use Gemini AI assistance.
Use product catalog information.
Calculate estimated spending.
Display remaining budget.
Provide fallback results when required.
Present the result through a web interface.

26. Demonstration Video Plan

A demonstration video should be prepared according to the SmartBridge submission requirements.

The video should include:

Screen sharing.
Voice-over explanation.
Project name.
Project purpose.
Problem statement.
Proposed solution.
Benefits.
Application execution.
Main features.
Working process.
Final output.
GitHub/project documentation overview.

Introduction
    |
    v
Project Name
    |
    v
Problem Statement
    |
    v
Proposed Solution
    |
    v
Technology Stack
    |
    v
Application Startup
    |
    v
Registration
    |
    v
Login
    |
    v
Planning Input
    |
    v
Budget Planning
    |
    v
Gemini AI Recommendation
    |
    v
Final Recommendation
    |
    v
Testing
    |
    v
GitHub Repository
    |
    v
Benefits
    |
    v
Conclusion

[ ] Application starts successfully
[ ] Home page loads correctly
[ ] Test user account is available
[ ] Login works
[ ] Planning input works
[ ] Budget calculation works
[ ] Recommendation result works
[ ] Gemini AI integration is configured
[ ] Fallback functionality is available
[ ] API documentation works
[ ] Automated tests pass
[ ] GitHub repository is accessible
[ ] Phase-wise documentation is complete
[ ] Screen sharing is enabled
[ ] Voice-over is clear
[ ] No API keys are visible
[ ] No passwords or personal credentials are visible
[ ] Final output is shown

[ ] Phase 1 – Brainstorming and Ideation
[ ] Phase 2 – Requirement Analysis
[ ] Phase 3 – Project Design
[ ] Phase 4 – Project Planning
[ ] Phase 5 – Project Development
[ ] Phase 6 – Project Testing
[ ] Phase 7 – Project Documentation
[ ] Phase 8 – Project Demonstration

[ ] Source code complete
[ ] README updated
[ ] requirements.txt available
[ ] .gitignore configured
[ ] Sensitive files excluded
[ ] Automated tests available
[ ] Tests verified
[ ] GitHub repository updated
[ ] Application verified
[ ] Demonstration video recorded
[ ] Demonstration video uploaded
[ ] Google Drive sharing permission verified
[ ] Final submission information prepared



```text
Phase 1 – Brainstorming & Ideation       ✅
Phase 2 – Requirement Analysis          ✅
Phase 3 – Project Design                ✅
Phase 4 – Project Planning              ✅
Phase 5 – Project Development           ✅
Phase 6 – Project Testing               ✅
Phase 7 – Project Documentation         ✅
Phase 8 – Project Demonstration         ✅