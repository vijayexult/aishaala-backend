from sqladmin import ModelView

from models import User, get_hashed_password

class UserAdminView(ModelView, model=User):
    column_list = ["id", "name", "email", "mobile", "is_active", "is_verified"]
    column_details_exclude_list = ["password"]
    form_columns = ["name", "email", "password", "mobile", "is_active"]
    
    async def insert_model(self, request, data):
        if "id" not in data and "password" in data:
            data["password"] = get_hashed_password(data["password"])
        return await super().insert_model(request, data)
