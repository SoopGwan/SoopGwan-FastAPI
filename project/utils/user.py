from sqlalchemy.orm import Session
from project.core.models.user import User
from fastapi import HTTPException, status, Response, Depends
from fastapi.security import OAuth2PasswordBearer
from project.core.models import Redis
from project.core import session_scope
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from project.core.config import API_KEY, API_SECRET, PHONE_NUMBER
from passlib.context import CryptContext
from datetime import datetime, timedelta
from project.core.config import JWT_ACCESS_TIMEOUT, REFRESH_ACCESS_TIMEOUT, SECRET, ALGORITHM
import jwt
import json
import random

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def check_id(account_id: str, session: Session):
    user = session.query(User.account_id).filter(User.account_id == account_id)

    if user.all():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="아이디 중복")

    else:
        return "success"


def send_code(phone_number: str):
    code = str(random.randint(1, 9999)).zfill(4)
    count = dict(json.loads(Redis.get(name=phone_number).decode('utf-8')))['count'] if Redis.get(name=phone_number) else 0
    if count >= 5:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS)
    data = {
        "code": code,
        "count": count + 1
    }
    Redis.setex(name=phone_number,
                value=json.dumps(data, ensure_ascii=False).encode('utf-8'),
                time=300)
    params = dict()
    params['type'] = 'sms'
    params['to'] = phone_number
    params['from'] = PHONE_NUMBER
    params['text'] = f"[숲관] 회원가입 인증코드 입니다. : {code}"
    cool = Message(API_KEY, API_SECRET)
    try:
        cool.send(params)
    except CoolsmsException as e:
        raise Response(status_code=e.code)
    return HTTPException(status_code=status.HTTP_200_OK)

def verify_code(phone_number:str, code:str):
    if Redis.get(name=phone_number):
        if code == dict(json.loads(Redis.get(name=phone_number).decode('utf-8')))['code']:
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증코드가 맞지 않음.")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증코드 사용가능 시간이 지남.")

def sign_up(phone_number: str, account_id: str, password: str, session: Session):
    check_id(account_id=account_id, session=session)
    session.add(
        User(
            phone_number=phone_number,
            account_id=account_id,
            password=password_hash(password)
        )
    )

    return {
        "access_token": create_access_token(account_id),
        "refresh_token": create_refresh_token(account_id)
    }

def password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(account_id: str):
    exp = datetime.utcnow() + timedelta(hours=JWT_ACCESS_TIMEOUT + 9)
    encoded_jwt = jwt.encode({"exp": exp, "sub": account_id}, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(account_id: str):
    exp = datetime.utcnow() + timedelta(hours=REFRESH_ACCESS_TIMEOUT + 9)
    encoded_jwt = jwt.encode({"exp": exp, "sub": account_id, "type": "refresh"}, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def login(account_id:str, password:str, session:Session):
    user = session.query(User.account_id, User.password).filter(User.account_id == account_id)

    if not user.scalar():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="계정이 존재하지 않음")

    user = user.first()
    if not pwd_context.verify(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 맞지 않음")

    return {
        "access_token": create_access_token(account_id=account_id),
        "refresh_token": create_refresh_token(account_id=account_id)
    }

def change_password(password: str, new_password: str, account_id: int, session: Session):
    user = session.query(User).filter(User.account_id == account_id)

    if not user.scalar():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="계정이 존재하지 않음")

    user = user.first()

    if not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 맞지 않음")

    user.password = password_hash(new_password)
    return {
        "message": "success"
    }

def get_current_user(token: str = Depends(oauth2_scheme)):
    with session_scope() as session:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="인증 실패"
        )
        try:
            payload = jwt.decode(token, SECRET, algorithms=ALGORITHM)
            account_id = payload.get("sub")
            if account_id is None:
                raise credentials_exception
        except jwt.PyJWTError:
            raise credentials_exception
        user = session.query(User).filter(User.account_id == account_id)
        if not user.scalar():
            raise credentials_exception
        return user.first()