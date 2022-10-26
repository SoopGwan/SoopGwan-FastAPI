from sqlalchemy.orm import Session
from project.core.models.user import User
from fastapi import HTTPException, status

def check_id(account_id: str, session: Session):
    user = session.query(User.account_id).filter(User.account_id == account_id)

    if user.scalar():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Overlap")

    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT)