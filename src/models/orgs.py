from uuid import uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, JSON, String, Text, Uuid
from sqlalchemy.orm import mapped_column, relationship

from .base import Base
from .users import User

class Org(Base):
    __tablename__ = "orgs"
    
    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = uuid4()
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id}, {self.name}, email: {self.email}"

    id = mapped_column(Uuid, primary_key=True, default=uuid4)
    name = mapped_column(String(256), nullable=False)
    legal_name = mapped_column(String(256), nullable=True)
    email = mapped_column(String(256))
    phone = mapped_column(String(13))
    website = mapped_column(String(256))
    address = mapped_column(Text)
    pin_code = mapped_column(String(6))
    admin_id = mapped_column(ForeignKey(User.id), nullable=False)
    admin = relationship("User", backref="orgs")
    is_active = mapped_column(Boolean(), default=False)
    # created_on = mapped_column(DateTime(), nullable=False)
    # created_by = mapped_column(ForeignKey(User.id), nullable=False)
    # approved_on = mapped_column(DateTime(), nullable=True)
    # approved_by = mapped_column(ForeignKey(User.id), nullable=False)
    logo = mapped_column(String(256))
    meta = mapped_column(JSON)


# class OrgSubscription(Base):
#     __tablename__ = "org_subscriptions"
    
#     def __init__(self, **kwargs):
#         if 'id' not in kwargs:
#             kwargs['id'] = uuid4()
#         super().__init__(**kwargs)

#     def __repr__(self):
#         return f"{self.id}, {self.org_id}, {self.plan_id}"

#     id = mapped_column(Uuid, primary_key=True, default=uuid4)
#     org_id = mapped_column(ForeignKey(Org.id), nullable=False)
#     org = relationship("Org", backref="org_subscriptions")
#     user_id = mapped_column(ForeignKey(User.id), nullable=False)
#     user = relationship("User", backref="user_subscriptions")
#     plan_id = mapped_column(ForeignKey(Plan.id), nullable=False)
#     plan = relationship("Plan", backref="plan")
#     is_active = mapped_column(Boolean(), default=False)
#     expiry_date = mapped_column(DateTime(), nullable=False)
    # meta = mapped_column(JSON)


# class Plan(Base):
#     __tablename__ = "student_plans"
    
#     def __init__(self, **kwargs):
#         if 'id' not in kwargs:
#             kwargs['id'] = uuid4()
#         super().__init__(**kwargs)

#     def __repr__(self):
#         return f"{self.id}, {self.name}, {self.description}"

#     id = mapped_column(Uuid, primary_key=True, default=uuid4)
#     name = mapped_column(String(256), nullable=False)
#     description = mapped_column(Text)
#     price = mapped_column(String(256), nullable=False)
#     duration = mapped_column(String(256), nullable=False)
#     is_active = mapped_column(Boolean(), default=False)
#     created_on = mapped_column(DateTime(), nullable=False)
#     created_by = mapped_column(ForeignKey(User.id), nullable=False)
#     updated_on = mapped_column(DateTime(), nullable=True)
#     updated_by = mapped_column(ForeignKey(User.id), nullable=False)
#     meta = mapped_column(JSON)
