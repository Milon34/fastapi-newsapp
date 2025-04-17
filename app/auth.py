from datetime import datetime, timedelta
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, CLIENT_ID, CLIENT_SECRET

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

CLIENTS = {
    CLIENT_ID: CLIENT_SECRET
}


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_client_credentials(client_id: str, client_secret: str):
    if CLIENTS.get(client_id) == client_secret:
        return True
    raise HTTPException(status_code=401, detail="Invalid client credentials")
