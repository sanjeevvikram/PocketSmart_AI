from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import get_settings
from .database import Base, engine
from .routes.api import router as api_router
from .routes.pages import router as page_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

settings=get_settings()
app=FastAPI(title=settings.app_name,version="1.0.0",description="Budget-aware AI recommendation assistant",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=[x.strip() for x in settings.frontend_origins.split(",")],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.mount("/static",StaticFiles(directory=str(Path(__file__).parent/"static")),name="static")
app.include_router(page_router)
app.include_router(api_router)

@app.get("/health")
def health(): return {"status":"ok","ai_configured":bool(settings.gemini_api_key),"model":settings.gemini_model}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=True)
