from sqlalchemy.orm import Session
from project.core.models.user import User
from fastapi import HTTPException, status
from project.core.models import Redis
from sdk.api.message import Message
from project.core.config import API_KEY, API_SECRET, PHONE_NUMBER
import json

import random

def check_id(account_id: str, session: Session):
    user = session.query(User.account_id).filter(User.account_id == account_id)

    if user.scalar():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Overlap")

    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


def send_code(phone_number: str):
    code = str(random.randint(1, 9999)).zfill(4)
    count = dict(json.loads(Redis.get(name="01034242475").decode('utf-8')))['count'] if Redis.get(name="01034242475") else 0
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
    Message(API_KEY, API_SECRET).send(params)
    return HTTPException(status_code=status.HTTP_200_OK)