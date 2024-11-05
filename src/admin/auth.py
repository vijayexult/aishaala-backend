from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from sqlalchemy.future import select
from sqladmin.authentication import AuthenticationBackend

from services import postgres
from models import User, verify_password

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        
        # Validate username/password credentials
        async with postgres.session() as db_session:
            statement = select(User).where(User.email == username)
            result = await db_session.execute(statement)
            user = result.scalars().first()
            if not user or not user.verify_password(password):
                return False

        # And update session
        request.session.update({"token": "..."})
        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")
