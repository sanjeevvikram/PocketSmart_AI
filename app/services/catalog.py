from dataclasses import dataclass
from urllib.parse import quote_plus

@dataclass(frozen=True)
class CatalogItem:
    title: str
    platform: str
    category: str
    price: float
    reason: str
    search_url: str

def _url(platform: str, query: str) -> str:
    q = quote_plus(query)
    urls = {
        "Amazon": f"https://www.amazon.in/s?k={q}",
        "Flipkart": f"https://www.flipkart.com/search?q={q}",
        "IKEA": f"https://www.ikea.com/in/en/search/?q={q}",
        "Swiggy": f"https://www.swiggy.com/search?query={q}",
        "Zomato": f"https://www.zomato.com/search?query={q}",
        "OYO": f"https://www.oyorooms.com/search?q={q}",
    }
    return urls.get(platform, f"https://www.google.com/search?q={q}")

def home_catalog(items: list[dict]) -> list[CatalogItem]:
    templates = {
        "light": [("Amazon", 1299), ("IKEA", 1799), ("Flipkart", 999)],
        "ceiling fan": [("Amazon", 2499), ("Flipkart", 2199), ("IKEA", 3299)],
        "dining table": [("IKEA", 9999), ("Amazon", 7999), ("Flipkart", 6499)],
        "sofa": [("IKEA", 19999), ("Amazon", 16999), ("Flipkart", 14999)],
        "wall art": [("IKEA", 2499), ("Amazon", 1299), ("Flipkart", 899)],
    }
    out=[]
    for item in items:
        key=item["name"].lower()
        matches=templates.get(key, [("Amazon", 1499), ("Flipkart", 1199), ("IKEA", 1699)])
        for platform, price in matches:
            out.append(CatalogItem(item["name"].title(), platform, "home", price, f"Demo match for requested {item['name']}", _url(platform,item["name"])))
    return out

def party_catalog(event_type: str) -> list[CatalogItem]:
    q=event_type.lower()
    return [
        CatalogItem(f"Catering options for {event_type}", "Swiggy", "catering", 2500, "Demo catering search", _url("Swiggy", q+" catering")),
        CatalogItem(f"Restaurant packages for {event_type}", "Zomato", "catering", 3000, "Demo restaurant search", _url("Zomato", q+" party")),
        CatalogItem(f"Event decor bundle", "Amazon", "decoration", 4500, "Demo decoration bundle", _url("Amazon", q+" party decoration")),
        CatalogItem(f"Stay/venue options", "OYO", "venue", 5000, "Demo accommodation/venue search", _url("OYO", q+" venue")),
    ]

def jewelry_catalog(style: str, occasion: str) -> list[CatalogItem]:
    query=f"{style} jewelry {occasion}"
    return [
        CatalogItem("Minimal pendant set", "Amazon", "jewelry", 2499, "Versatile option for the requested style", _url("Amazon",query)),
        CatalogItem("Elegant earrings set", "Flipkart", "jewelry", 1799, "Lightweight option suitable for occasions", _url("Flipkart",query)),
        CatalogItem("Classic statement necklace", "Amazon", "jewelry", 4999, "Statement piece for dressier styling", _url("Amazon",query)),
    ]
