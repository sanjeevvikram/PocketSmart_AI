from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .config import get_settings
from .database import get_db
from .models.db import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()
ALGORITHM = "HS256"
COOKIE = "pocketsmart_token"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_token(user_id: int) -> str:
    payload = {"sub": str(user_id), "exp": datetime.now(timezone.utc) + timedelta(hours=24)}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)

def current_user(request: Request, db: Session = Depends(get_db)) -> User:
    token = request.cookies.get(COOKIE)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        user_id = int(payload["sub"])
    except (JWTError, KeyError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired session")
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
