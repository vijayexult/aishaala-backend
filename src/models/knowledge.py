# from uuid import uuid4
# from sqlalchemy import Boolean, DateTime, ForeignKey, JSON, String, Text, Uuid
# from sqlalchemy.orm import mapped_column, relationship

# from .base import Base
# from .users import User

# class Knowledge(Base):
#   __tablename__ = "knowledge"
  
#   def __init__(self, **kwargs):
#         if 'id' not in kwargs:
#             kwargs['id'] = uuid4()
#         super().__init__(**kwargs)

#   id = mapped_column(Uuid, primary_key=True, default=uuid4)
#   type = mapped_column(String(64), nullable=False)
#   name = mapped_column(String(256), nullable=False)
#   content_source = mapped_column(Text(), nullable=False)
#   uploaded_date = mapped_column(DateTime(), nullable=False)
#   created_by = mapped_column(ForeignKey(User.id), nullable=False)
#   is_deleted = mapped_column(Boolean(), nullable=False, default=False)
#   is_processed = mapped_column(Boolean(), nullable=True, default=False)
#   meta = mapped_column(JSON)