from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class SessionResponse(BaseModel):
    authenticated: bool
    user: dict | None = None

class HomeItem(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    quantity: int = Field(default=1, ge=1, le=50)

class HomeRequest(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    rooms: list[str] = Field(min_length=1, max_length=10)
    items: list[HomeItem] = Field(min_length=1, max_length=30)
    style: str = Field(default="modern", max_length=80)
    notes: str = Field(default="", max_length=1000)

class PartyRequest(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    guests: int = Field(gt=0, le=5000)
    event_type: str = Field(min_length=2, max_length=80)
    venue: str = Field(default="home", max_length=120)
    date: str = Field(default="", max_length=40)
    preferences: str = Field(default="", max_length=1000)

class RecommendationItem(BaseModel):
    title: str
    platform: str
    category: str
    estimated_price: float = Field(ge=0)
    quantity: int = Field(default=1, ge=1)
    reason: str
    url: str

class RecommendationResponse(BaseModel):
    planner: str
    budget: float
    estimated_total: float
    budget_remaining: float
    allocation: dict[str, float] = {}
    summary: str
    recommendations: list[RecommendationItem]
    ai_generated: bool
    source_note: str

class JewelryRequest(BaseModel):
    budget: float = Field(gt=0, le=10_000_000)
    occasion: str = Field(min_length=2, max_length=80)
    outfit_description: str = Field(default="", max_length=1000)
    metal_preference: str = Field(default="any", max_length=50)
    style: str = Field(default="elegant", max_length=80)

class RecommendationEnvelope(BaseModel):
    model_config = ConfigDict(extra="ignore")
    planner: str
    request: dict
    result: RecommendationResponse
