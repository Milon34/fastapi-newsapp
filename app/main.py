from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import create_access_token, verify_client_credentials
from app.endpoints import news
from app.logging_config import setup_logging
import logging

app = FastAPI()


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if verify_client_credentials(form_data.username, form_data.password):
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}


app.include_router(news.router)

# Initialize logging
setup_logging()


@app.get("/")
def read_root():
    logging.info("Root endpoint was accessed")
    return {"message": "Hello, World!"}
