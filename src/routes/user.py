import logging

import aiohttp
from fastapi import APIRouter, Response, Depends
from fastapi.security import OAuth2PasswordBearer
# from jose import jwt

from aishaala_backend import settings
from utils.sms import send_login_otp
from schemas import *

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/otp')
async def post_otp(request: OtpRequest) -> OtpResponse:
    try:
        await send_login_otp(request.number, "1234")
        return {"status": "Success"}
    except Exception as e:
        logger.exception("Error sending otp", e)
        return {"status": "Failed"}

@router.get('/oauth/google')
async def login_google():
    return {
        "url": f"{settings.GOOGLE_OAUTH2_AUTH_URI}?response_type=code&client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&redirect_uri={settings.GOOGLE_OAUTH2_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    }

@router.get('/oauth/google/initiate')
async def login_google(response: Response):
    response.status_code = 302
    response.headers.update({
        "Location": f"{settings.GOOGLE_OAUTH2_AUTH_URI}?response_type=code&client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&redirect_uri={settings.GOOGLE_OAUTH2_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    })
    return ''

@router.get('/oauth/google/done')
async def login_google_done(code: str):
    data = {
        "code": code,
        "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
        "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_OAUTH2_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    async with aiohttp.ClientSession() as http_client:
        async with http_client.post(settings.GOOGLE_OAUTH2_TOKEN_URI,
                                json=data,
                                headers={
                                    'type': 'crm',
                                    'Content-Type': 'application/json'
                                }) as oauth_response:
            response = await oauth_response.json()
            print(response)
            access_token = response.get("access_token")
            # Save the token in DB
            if not access_token:
                return {"error": "Invalid access token"}
        async with http_client.get("https://www.googleapis.com/oauth2/v1/userinfo",
                                   headers={
                                       "Authorization": f"Bearer {access_token}"
                                    }) as user_info_response:
            user_info = await user_info_response.json()
            print(user_info)
            # Create a user and save in DB if not exists
            # create/update the access token
            if not user_info:
                return {"error": "Invalid user info"}
            return {"user": user_info}

@router.get("/")
async def get_knowledge():
    return {"knowledge": "knowledge"}

@router.post("/")
async def post_knowledge():
    return {"knowledge": "knowledge"}

@router.put("/")
async def put_knowledge():
    return {"knowledge": "knowledge"}

@router.delete("/")
async def delete_knowledge():
    return {"knowledge": "knowledge"}
