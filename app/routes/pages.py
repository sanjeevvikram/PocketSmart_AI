from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
router=APIRouter()
templates=Jinja2Templates(directory=str(Path(__file__).resolve().parent.parent/"templates"))

@router.get("/",response_class=HTMLResponse)
def index(request:Request): return templates.TemplateResponse("index.html",{"request":request})
@router.get("/login",response_class=HTMLResponse)
def login(request:Request): return templates.TemplateResponse("login.html",{"request":request,"mode":"login"})
@router.get("/register",response_class=HTMLResponse)
def register(request:Request): return templates.TemplateResponse("login.html",{"request":request,"mode":"register"})
@router.get("/dashboard",response_class=HTMLResponse)
def dashboard(request:Request): return templates.TemplateResponse("dashboard.html",{"request":request})
