from project.core import session_scope

from fastapi import APIRouter, HTTPException, status
from project.utils.user import check_id, send_code, verify_code, sign_up
from project.core.schemas.user import SendCode, VerifyCode, SignUp

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

@app.post("/signup")
async def signup_user(body: SignUp):
    with session_scope() as session:
        return sign_up(phone_number=body.phone_number, account_id=body.account_id, password=body.password, session=session)