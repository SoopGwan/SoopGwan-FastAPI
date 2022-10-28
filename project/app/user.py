from project.core import session_scope

from fastapi import APIRouter, HTTPException, status
from project.utils.user import check_id, send_code, verify_code, sign_up
from project.core.schemas.user import SendCode, VerifyCode, SignUp
import re

app = APIRouter()

@app.options("/check")
async def checking_id(account_id: str):
    with session_scope() as session:
        message = check_id(account_id=account_id, session=session)
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=message)

@app.post("/send")
async def sending_code(body: SendCode):
    return send_code(phone_number=body.phone_number)

@app.post("/verify")
async def verifying_code(body: VerifyCode):
    return verify_code(phone_number=body.phone_number, code=body.code)

@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup_user(body: SignUp):
    with session_scope() as session:
        REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
        if not re.fullmatch(REGEX_PASSWORD, body.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호 형식이 잘못됨")
        return sign_up(phone_number=body.phone_number, account_id=body.account_id, password=body.password, session=session)