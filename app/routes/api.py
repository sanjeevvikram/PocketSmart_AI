import json
from unittest import result
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..auth import current_user, create_token, hash_password, verify_password, COOKIE
from ..database import get_db
from ..models.db import Recommendation, User
from ..models.schemas import HomeRequest, PartyRequest, JewelryRequest, RegisterRequest, LoginRequest
from ..services.gemini_utils import generate
from fastapi.responses import JSONResponse

from app.models import db

router=APIRouter(prefix="/api")

def save_result(db,user,planner,request_data,result):
    row=Recommendation(user_id=user.id,planner=planner,request_json=json.dumps(request_data),response_json=json.dumps(result))
    db.add(row); db.commit(); db.refresh(row)
    return row

@router.post("/auth/register")
def register(data:RegisterRequest, db:Session=Depends(get_db)):
    if db.scalar(select(User).where(User.email==data.email.lower())):
        raise HTTPException(409,"Email already registered")
    user=User(email=data.email.lower(),password_hash=hash_password(data.password)); db.add(user); db.commit(); db.refresh(user)
    response=JSONResponse({"message":"Registered successfully","user":{"id":user.id,"email":user.email}}); response.set_cookie(COOKIE,create_token(user.id),httponly=True,samesite="lax",max_age=86400); return response

@router.post("/auth/login")
def login(data:LoginRequest, db:Session=Depends(get_db)):
    user=db.scalar(select(User).where(User.email==data.email.lower()))
    if not user or not verify_password(data.password,user.password_hash): raise HTTPException(401,"Invalid email or password")
    response=JSONResponse({"message":"Logged in","user":{"id":user.id,"email":user.email}}); response.set_cookie(COOKIE,create_token(user.id),httponly=True,samesite="lax",max_age=86400); return response

@router.post("/auth/logout")
def logout():
    response=JSONResponse({"message":"Logged out"}); response.delete_cookie(COOKIE); return response

@router.get("/auth/session-info")
def session_info(user:User=Depends(current_user)): return {"authenticated":True,"user":{"id":user.id,"email":user.email}}

@router.get("/auth/session-data")
def session_data(user:User=Depends(current_user),db:Session=Depends(get_db)):
    count=db.scalar(select(Recommendation).where(Recommendation.user_id==user.id).count()) if False else len(user.recommendations)
    return {"user":{"id":user.id,"email":user.email},"recommendation_count":count}

@router.post("/generate-home")
def home(data:HomeRequest,user:User=Depends(current_user),db:Session=Depends(get_db)):
    result=generate("home",data.model_dump()); save_result(db,user,"home",data.model_dump(),result); return result

@router.post("/generate-party")
def party(data:PartyRequest,user:User=Depends(current_user),db:Session=Depends(get_db)):
    result=generate("party",data.model_dump()); save_result(db,user,"party",data.model_dump(),result); return result

@router.post("/generate-jewelry")
async def jewelry(budget:float=Form(...),occasion:str=Form(...),outfit_description:str=Form(""),metal_preference:str=Form("any"),style:str=Form("elegant"),outfit_image:UploadFile|None=File(None),user:User=Depends(current_user),db:Session=Depends(get_db)):
    data=JewelryRequest(budget=budget,occasion=occasion,outfit_description=outfit_description,metal_preference=metal_preference,style=style).model_dump()
    image_bytes=None; mime=None
    if outfit_image:
        if not outfit_image.content_type or not outfit_image.content_type.startswith("image/"): raise HTTPException(400,"outfit_image must be an image")
        image_bytes=await outfit_image.read()
        if len(image_bytes)>5*1024*1024: raise HTTPException(413,"Image must be <= 5 MB")
        mime=outfit_image.content_type
    result = generate("jewelry", data)
    save_result(db, user, "jewelry", data, result)
    return result

@router.get("/history")
def history(user:User=Depends(current_user),db:Session=Depends(get_db)):
    rows=db.scalars(select(Recommendation).where(Recommendation.user_id==user.id).order_by(Recommendation.created_at.desc()).limit(50)).all()
    return [{"id":r.id,"planner":r.planner,"created_at":r.created_at.isoformat(),"request":json.loads(r.request_json)} for r in rows]

@router.get("/recommendations/{recommendation_id}")
def recommendation(recommendation_id:int,user:User=Depends(current_user),db:Session=Depends(get_db)):
    r=db.scalar(select(Recommendation).where(Recommendation.id==recommendation_id,Recommendation.user_id==user.id))
    if not r: raise HTTPException(404,"Recommendation not found")
    return json.loads(r.response_json)
