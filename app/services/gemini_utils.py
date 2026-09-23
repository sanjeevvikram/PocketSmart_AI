import json
from typing import Any
from google import genai
from google.genai import types
from .catalog import home_catalog, party_catalog, jewelry_catalog
from ..config import get_settings

settings=get_settings()

def _client():
    if not settings.gemini_api_key:
        return None
    return genai.Client(api_key=settings.gemini_api_key)

def _fallback_home(data: dict) -> dict:
    budget=data["budget"]
    candidates=home_catalog(data["items"])
    rec=[]; total=0
    for c in candidates:
        qty=next((x["quantity"] for x in data["items"] if x["name"].lower()==c.title.lower()),1)
        price=c.price*qty
        if total+price <= budget*0.92:
            rec.append({"title":c.title,"platform":c.platform,"category":c.category,"estimated_price":c.price,"quantity":qty,"reason":c.reason,"url":c.search_url}); total+=price
    if not rec and candidates:
        c=candidates[0]; rec=[{"title":c.title,"platform":c.platform,"category":c.category,"estimated_price":c.price,"quantity":1,"reason":c.reason,"url":c.search_url}]; total=c.price
    return {"planner":"home","budget":budget,"estimated_total":round(total,2),"budget_remaining":round(budget-total,2),"allocation":{"furniture":round(total*.5,2),"lighting":round(total*.2,2),"decor":round(total*.3,2)},"summary":f"Fallback plan for a {data['style']} home setup.","recommendations":rec,"ai_generated":False,"source_note":"Demo catalog/search links; prices are illustrative and should be verified on the platform before purchase."}

def _fallback_party(data: dict) -> dict:
    budget=data["budget"]; alloc={"catering":budget*.45,"decoration":budget*.2,"entertainment":budget*.15,"venue":budget*.2}
    rec=[]
    for c in party_catalog(data["event_type"]):
        share=alloc.get(c.category, budget*.1)
        if share>0: rec.append({"title":c.title,"platform":c.platform,"category":c.category,"estimated_price":round(min(c.price,share),2),"quantity":1,"reason":c.reason,"url":c.search_url})
    total=sum(x["estimated_price"] for x in rec)
    return {"planner":"party","budget":budget,"estimated_total":round(total,2),"budget_remaining":round(max(0,budget-total),2),"allocation":{k:round(v,2) for k,v in alloc.items()},"summary":f"Budget allocation for {data['event_type']} with {data['guests']} guests.","recommendations":rec,"ai_generated":False,"source_note":"Demo vendor/search links; availability and pricing must be verified."}

def _fallback_jewelry(data: dict) -> dict:
    budget=data["budget"]; rec=[]; total=0
    for c in jewelry_catalog(data["style"],data["occasion"]):
        if total+c.price<=budget: rec.append({"title":c.title,"platform":c.platform,"category":c.category,"estimated_price":c.price,"quantity":1,"reason":c.reason,"url":c.search_url}); total+=c.price
    return {"planner":"jewelry","budget":budget,"estimated_total":round(total,2),"budget_remaining":round(budget-total,2),"allocation":{"necklace":round(total*.5,2),"earrings":round(total*.3,2),"accent":round(total*.2,2)},"summary":f"{data['style'].title()} jewelry ideas for {data['occasion']}.","recommendations":rec,"ai_generated":False,"source_note":"Demo search links; prices are illustrative and should be verified before purchase."}

def _clean_json(text: str) -> dict:
    text=text.strip()
    if text.startswith("```"):
        text=text.split("\n",1)[1].rsplit("```",1)[0]
    return json.loads(text)

def generate(planner: str, data: dict, image_bytes: bytes|None=None, mime_type: str|None=None) -> dict:
    client=_client()
    fallback={"home":_fallback_home,"party":_fallback_party,"jewelry":_fallback_jewelry}[planner](data)
    if not client:
        return fallback
    prompt=f"""You are PocketSmart AI, a budget-aware recommendation assistant. Planner={planner}.\nUser data={json.dumps(data, ensure_ascii=False)}\nReturn ONLY valid JSON matching this schema: {{planner,budget,estimated_total,budget_remaining,allocation,summary,recommendations:[{{title,platform,category,estimated_price,quantity,reason,url}}],ai_generated,source_note}}.\nDo not invent real-time availability. Platform links may be search URLs. Keep estimated_total <= budget. Use concise reasons. Mark ai_generated true and explain that prices/availability require verification."""
    contents: list[Any]=[prompt]
    if image_bytes and mime_type:
        contents.insert(0, types.Part.from_bytes(data=image_bytes, mime_type=mime_type))
        contents.insert(1, "Analyze the uploaded outfit image only for non-sensitive visible fashion characteristics relevant to jewelry matching.")
    try:
        response=client.models.generate_content(model=settings.gemini_model, contents=contents, config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=4000))
        result=_clean_json(response.text)
        result["ai_generated"]=True
        result.setdefault("source_note","AI-generated recommendations; prices and availability must be verified.")
        return result
    except Exception:
        return fallback
