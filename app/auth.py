
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserLogin
from app.security import verify_password, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# User Login API
@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    # Find user by username
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    # Check username
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Verify password
    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create JWT token
    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
