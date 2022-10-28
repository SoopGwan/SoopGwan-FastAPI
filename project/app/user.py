from project.core import session_scope

from fastapi import APIRouter, HTTPException, status, Response, Depends
from project.utils.user import check_id, send_code, verify_code, sign_up, login, change_password, get_current_user
from project.core.schemas.user import SendCode, VerifyCode, SignUp, Login, ChangePassword
from project.core.models.user import User
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

@app.post("/login")
async def logins(body: Login):
    with session_scope() as session:
        return login(account_id=body.account_id, password=body.password, session=session)

@app.patch("/change", status_code=status.HTTP_204_NO_CONTENT)
async def changing_password(body: ChangePassword, user: User = Depends(get_current_user)):
    with session_scope() as session:
        change_password(password=body.password, new_password=body.new_password, account_id=user.account_id, session=session)
        return Response(status_code=204)