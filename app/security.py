
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from pwdlib import PasswordHash


# Password hashing configuration
password_hash = PasswordHash.recommended()


# JWT configuration
SECRET_KEY = "cy1vD13vS6ryUuShu1afZQ7XNMo-X5kFL0fcYjl8LJ0"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Hash password
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Verify password
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )


# Create JWT access token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# Decode JWT access token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:
        return None
