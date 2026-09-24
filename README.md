---

## Development Phases

### Phase 1 — Gemini Initialization

**Status: Completed ✅**

- Initialized Gemini API integration.
- Installed the Google Gemini Python SDK.
- Added `google-genai==1.11.0` to `requirements.txt`.
- Added Gemini configuration support through `.env`.
- Configured `GEMINI_MODEL=gemini-2.5-flash`.
- Verified that the Gemini SDK is installed in the project virtual environment.
- Kept the Gemini API key in the local `.env` file and excluded `.env` from Git.

**Next Phase:** Gemini service layer integration.

### Phase 2 — Gemini Service Layer

**Status: Pending ⏳**

- Create the Gemini service layer.
- Connect the service to the existing PocketSmart AI backend.
- Test Gemini communication.
- Handle Gemini API errors safely.

### Phase 3 — AI Recommendation Integration

**Status: Pending ⏳**

- Connect Gemini recommendations to the existing planners.
- Generate structured recommendation responses.
- Test Party and Home planning flows.

### Phase 4 — Jewelry AI Integration

**Status: Pending ⏳**

- Connect Gemini to jewelry planning.
- Support jewelry image analysis.
- Generate AI-based jewelry recommendations.

### Phase 5 — Testing & Validation

**Status: Pending ⏳**

- Test all Gemini-powered features.
- Run the complete test suite.
- Fix integration issues.
- Verify authentication and existing functionality.

### Phase 6 — Final GitHub Release

**Status: Pending ⏳**

- Finalize README documentation.
- Review project configuration.
- Commit final changes.
- Push the completed project to GitHub.


    # PocketSmart AI

A FastAPI + Jinja2 + Gemini application based on the supplied PocketSmart AI project documentation. It provides authenticated Home, Party, and Jewelry budget planners, recommendation history, mock platform sourcing, and optional Gemini multimodal analysis for jewelry images.

> The source document names Gemini 1.5 Flash Pro, while current Google Gemini API documentation uses newer model IDs. This implementation keeps the model configurable via `GEMINI_MODEL` and defaults to `gemini-2.5-flash`. Change it to an available model in your account if required.

## Features
- Register/login/logout with JWT stored in an HTTP-only cookie.
- Home planner: room/item quantities, budget, style.
- Party planner: event, guests, venue, catering/decor/entertainment allocation.
- Jewelry planner: occasion, outfit description, budget, optional image upload.
- Gemini structured JSON recommendation generation when `GEMINI_API_KEY` is configured.
- Deterministic fallback recommendations when Gemini is unavailable.
- Mock cross-platform catalog data for Amazon, Flipkart, IKEA, Swiggy, Zomato, and OYO-style results; clearly marked as demo data.
- SQLite recommendation history.
- Responsive frontend.
- API docs at `/docs`.

## Quick start (VS Code)
1. Open this folder in VS Code.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it (Windows PowerShell): `.venv\\Scripts\\Activate.ps1`
4. Install: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and set `SECRET_KEY`. Add `GEMINI_API_KEY` for live AI.
6. Run: `uvicorn app.main:app --reload`
7. Open http://127.0.0.1:8000
8. Register a user, then try each planner.

## API
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/logout`
- `GET /api/auth/session-info`
- `GET /api/auth/session-data`
- `POST /api/generate-home`
- `POST /api/generate-party`
- `POST /api/generate-jewelry`
- `GET /api/history`
- `GET /api/recommendations/{id}`
- `GET /health`

## Testing
Run `pytest -q`.

The test suite exercises validation, fallback recommendation generation, and core API routes without requiring a Gemini key.
