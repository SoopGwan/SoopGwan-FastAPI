from project.core import session_scope

from fastapi import APIRouter
from project.utils.user import check_id, send_code
from project.core.schemas.user import SendCode

app = APIRouter()

@app.options("/check")
async def checking_id(account_id: str):
    with session_scope() as session:
        return check_id(account_id=account_id, session=session)

@app.post("/send")
async def sending_code(body: SendCode):
    with session_scope() as session:
        return send_code(body.phone_number)