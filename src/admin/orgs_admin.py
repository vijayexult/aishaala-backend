from sqladmin import ModelView

from models import Org

class OrgAdminView(ModelView, model=Org):
    column_list = ["id", "name", "email", "website", "phone", "is_active"]
    form_columns = ["name", "email", "website", "phone", "is_active", "admin", "address", "pin_code", "logo"]
