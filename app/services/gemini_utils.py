import json
import os
from typing import Any

from google import genai

from app.config import settings


def get_client():
    """Create and return the Gemini client."""
    api_key = getattr(settings, "gemini_api_key", None) or os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    return genai.Client(api_key=api_key)


def _safe_fallback(planner: str, data: dict) -> dict:
    """Create a useful local fallback when Gemini is unavailable."""

    budget = float(data.get("budget", 0) or 0)

    # ---------------------------------------------------------
    # HOME FALLBACK
    # ---------------------------------------------------------
    if planner == "home":
        allocation = {
            "furniture": round(budget * 0.45, 2),
            "lighting": round(budget * 0.20, 2),
            "decor": round(budget * 0.20, 2),
            "reserve": round(budget * 0.15, 2),
        }

        items = data.get("items", [])
        recommendations = []

        for item in items:
            name = str(item.get("name", "Home item"))
            quantity = int(item.get("quantity", 1) or 1)

            name_lower = name.lower()

            if "light" in name_lower:
                price = 1500
                category = "Lighting"
            elif "fan" in name_lower:
                price = 3500
                category = "Appliances"
            elif "table" in name_lower:
                price = 5000
                category = "Furniture"
            else:
                price = 2000
                category = "Home"

            recommendations.append(
                {
                    "title": name.title(),
                    "platform": "Online Search",
                    "category": category,
                    "estimated_price": float(price),
                    "quantity": quantity,
                    "reason": f"Recommended for your {planner} plan.",
                    "url": (
                        "https://www.google.com/search?q="
                        + name.replace(" ", "+")
                    ),
                }
            )

        estimated_total = sum(
            item["estimated_price"] * item["quantity"]
            for item in recommendations
        )

        if estimated_total > budget and budget > 0:
            estimated_total = budget

        return {
            "planner": planner,
            "budget": budget,
            "estimated_total": float(estimated_total),
            "budget_remaining": float(max(0, budget - estimated_total)),
            "allocation": allocation,
            "summary": "Budget-based home setup plan.",
            "recommendations": recommendations,
            "ai_generated": False,
            "source_note": (
                "Fallback plan; prices are illustrative and should "
                "be verified before purchase."
            ),
        }

    # ---------------------------------------------------------
    # PARTY FALLBACK
    # ---------------------------------------------------------
    if planner == "party":
        guests = int(data.get("guests", 0) or 0)
        event_type = str(data.get("event_type", "event"))

        allocation = {
            "food": round(budget * 0.40, 2),
            "decoration": round(budget * 0.20, 2),
            "venue": round(budget * 0.20, 2),
            "reserve": round(budget * 0.20, 2),
        }

        recommendations = [
            {
                "title": "Food and Refreshments",
                "platform": "Online Search",
                "category": "Food",
                "estimated_price": float(allocation["food"]),
                "quantity": 1,
                "reason": f"Planned for {guests} guests.",
                "url": (
                    "https://www.google.com/search?q="
                    "party+food+and+refreshments"
                ),
            },
            {
                "title": "Event Decorations",
                "platform": "Online Search",
                "category": "Decoration",
                "estimated_price": float(allocation["decoration"]),
                "quantity": 1,
                "reason": f"Suitable for a {event_type} event.",
                "url": (
                    "https://www.google.com/search?q="
                    "party+decorations"
                ),
            },
            {
                "title": "Venue",
                "platform": "Online Search",
                "category": "Venue",
                "estimated_price": float(allocation["venue"]),
                "quantity": 1,
                "reason": "Budget allocation for the event venue.",
                "url": (
                    "https://www.google.com/search?q="
                    "party+venue"
                ),
            },
        ]

        estimated_total = sum(
            item["estimated_price"] * item["quantity"]
            for item in recommendations
        )

        return {
            "planner": planner,
            "budget": budget,
            "estimated_total": float(estimated_total),
            "budget_remaining": float(max(0, budget - estimated_total)),
            "allocation": allocation,
            "summary": f"Budget-based plan for a {event_type} party.",
            "recommendations": recommendations,
            "ai_generated": False,
            "source_note": (
                "Fallback plan; prices are illustrative and should "
                "be verified before purchase."
            ),
        }

    # ---------------------------------------------------------
    # JEWELRY FALLBACK
    # ---------------------------------------------------------
    if planner == "jewelry":
        allocation = {
            "jewelry": round(budget * 0.70, 2),
            "accessories": round(budget * 0.15, 2),
            "reserve": round(budget * 0.15, 2),
        }

        recommendations = [
            {
                "title": "Jewelry",
                "platform": "Online Search",
                "category": "Jewelry",
                "estimated_price": float(allocation["jewelry"]),
                "quantity": 1,
                "reason": "Main jewelry budget allocation.",
                "url": (
                    "https://www.google.com/search?q="
                    "jewelry"
                ),
            },
            {
                "title": "Accessories",
                "platform": "Online Search",
                "category": "Accessories",
                "estimated_price": float(allocation["accessories"]),
                "quantity": 1,
                "reason": "Additional accessory allocation.",
                "url": (
                    "https://www.google.com/search?q="
                    "jewelry+accessories"
                ),
            },
        ]

        estimated_total = sum(
            item["estimated_price"] * item["quantity"]
            for item in recommendations
        )

        return {
            "planner": planner,
            "budget": budget,
            "estimated_total": float(estimated_total),
            "budget_remaining": float(max(0, budget - estimated_total)),
            "allocation": allocation,
            "summary": "Budget-based jewelry plan.",
            "recommendations": recommendations,
            "ai_generated": False,
            "source_note": (
                "Fallback plan; prices are illustrative and should "
                "be verified before purchase."
            ),
        }

    # ---------------------------------------------------------
    # GENERIC FALLBACK
    # ---------------------------------------------------------
    return {
        "planner": planner,
        "budget": budget,
        "estimated_total": 0.0,
        "budget_remaining": budget,
        "allocation": {
            "main": round(budget * 0.60, 2),
            "support": round(budget * 0.25, 2),
            "reserve": round(budget * 0.15, 2),
        },
        "summary": f"Fallback plan for a {planner}.",
        "recommendations": [],
        "ai_generated": False,
        "source_note": (
            "Fallback plan; prices are illustrative and should "
            "be verified before purchase."
        ),
    }


def generate(planner: str, data: dict) -> dict:
    """Generate a plan using Gemini, with a safe local fallback."""

    client = get_client()

    # Always prepare a safe fallback first.
    fallback = _safe_fallback(planner, data)

    # If Gemini is not configured, use fallback.
    if client is None:
        print("GEMINI NOT CONFIGURED - USING FALLBACK PLAN")
        return fallback

    model = getattr(
        settings,
        "gemini_model",
        None,
    ) or os.getenv(
        "GEMINI_MODEL",
        "gemini-3.6-flash",
    )

    prompt = f"""
You are PocketSmart AI, a budget planning assistant.

Create a practical budget plan.

Planner:
{planner}

User data:
{json.dumps(data, indent=2)}

Return ONLY valid JSON with this structure:

{{
  "planner": "{planner}",
  "budget": 0,
  "estimated_total": 0,
  "budget_remaining": 0,
  "allocation": {{}},
  "summary": "",
  "recommendations": [],
  "ai_generated": true,
  "source_note": ""
}}

Each recommendation should contain:
- title
- platform
- category
- estimated_price
- quantity
- reason
- url
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )

        text = getattr(response, "text", None)

        if not text:
            print("GEMINI RETURNED NO TEXT - USING FALLBACK PLAN")
            return fallback

        text = text.strip()

        # Remove Markdown JSON fences if Gemini adds them.
        if text.startswith("```"):
            lines = text.splitlines()

            if lines and lines[0].startswith("```"):
                lines = lines[1:]

            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]

            text = "\n".join(lines).strip()

        result = json.loads(text)

        if not isinstance(result, dict):
            print("GEMINI RETURNED INVALID JSON - USING FALLBACK PLAN")
            return fallback

        result.setdefault("planner", planner)
        result.setdefault("budget", float(data.get("budget", 0) or 0))
        result.setdefault("estimated_total", 0.0)

        estimated_total = float(
            result.get("estimated_total", 0) or 0
        )

        budget = float(
            result.get("budget", data.get("budget", 0)) or 0
        )

        result["budget_remaining"] = float(
            max(0, budget - estimated_total)
        )

        result.setdefault("allocation", {})
        result.setdefault("summary", "AI-generated budget plan.")
        result.setdefault("recommendations", [])
        result["ai_generated"] = True
        result.setdefault(
            "source_note",
            "Generated using Gemini AI.",
        )

        return result

    except Exception as exc:
        print(f"GEMINI FAILED - USING FALLBACK PLAN: {exc}")
        return fallback