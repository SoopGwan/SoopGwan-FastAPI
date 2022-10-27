from project.core import session_scope

from fastapi import APIRouter
from project.utils.user import check_id, send_code, verify_code
from project.core.schemas.user import SendCode, VerifyCode

app = APIRouter()

@app.options("/check")
async def checking_id(account_id: str):
    with session_scope() as session:
        return check_id(account_id=account_id, session=session)

@app.post("/send")
async def sending_code(body: SendCode):
    return send_code(phone_number=body.phone_number)

@app.post("/verify")
async def verifying_code(body: VerifyCode):
    return verify_code(phone_number=body.phone_number, code=body.code)