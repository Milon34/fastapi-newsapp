from dotenv import load_dotenv
import os

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BASE_URL = os.getenv("BASE_URL")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
ALGORITHM = os.getenv("ALGORITHM", "HS256")
APP_ENV = os.getenv("APP_ENV")
