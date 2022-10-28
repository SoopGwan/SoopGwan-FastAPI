from project.core import session_scope

from fastapi import APIRouter, HTTPException, status, Response
from project.utils.user import check_id, send_code, verify_code, sign_up
from project.core.schemas.user import SendCode, VerifyCode, SignUp
import re

app = APIRouter()

@app.options("/check", status_code=status.HTTP_204_NO_CONTENT)
async def checking_id(account_id: str):
    with session_scope() as session:
        REGEX_ID = r'^[A-Za-z0-9]{6,24}$'
        if not re.fullmatch(REGEX_ID, account_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="아이디 형식이 잘못됨.")
        check_id(account_id=account_id, session=session)
        return Response(status_code=204)

@app.post("/send")
async def sending_code(body: SendCode):
    return send_code(phone_number=body.phone_number)

@app.post("/verify")
async def verifying_code(body: VerifyCode):
    return verify_code(phone_number=body.phone_number, code=body.code)

@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup_user(body: SignUp):
    with session_scope() as session:
        return sign_up(phone_number=body.phone_number, account_id=body.account_id, password=body.password, session=session)