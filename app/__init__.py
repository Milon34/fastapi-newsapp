from app.database import engine, Base
from app.models import News

Base.metadata.create_all(bind=engine)
