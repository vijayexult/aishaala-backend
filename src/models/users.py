from uuid import uuid4
from passlib.context import CryptContext
from sqlalchemy import Boolean, DateTime, ForeignKey, JSON, String, Uuid 
from sqlalchemy.orm import mapped_column, relationship

from .base import Base

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

class User(Base):
    __tablename__ = "users"
    
    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = uuid4()
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.email}"

    id = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name = mapped_column(String(64), nullable=False)
    email = mapped_column(String(256), unique=True)
    mobile = mapped_column(String(13), unique=True)
    password = mapped_column(String(1024), nullable=True)
    is_active = mapped_column(Boolean(), default=True)
    is_verified = mapped_column(Boolean(), default=False)
    # created_on = mapped_column(DateTime(), nullable=False)

    def verify_password(self, password: str) -> bool:
        return verify_password(password, self.password)


# class GoogleOauth(Base):
#     __tablename__ = "google_oauth"

#     def __repr__(self):
#         return f"{self.id}, {self.user_id}, {self.oauth_id}"

#     user_id = mapped_column(ForeignKey(User.id), unique=True, nullable=False)
#     user = relationship("User", backref="google_auth", uselist=False)
#     token = mapped_column(String(1024), nullable=False)
#     expiry = mapped_column(DateTime(), nullable=False)
#     meta = mapped_column(JSON)
