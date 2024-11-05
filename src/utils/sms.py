import aiohttp
import random
import logging
import string

logger = logging.getLogger(__name__)


def id_generator(size=5, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

async def send_login_otp(number, otp):
    if otp is None:
        otp = "".join([random.choice(string.digits) for _ in range(6)])
    logger.debug(f"Mobile: {number} OTP: {otp}")
    # cache.set(MOBILE_OTP_KEY % number, otp, OTP_TIME_LIMIT)
    return await send_sms(number, f"{otp} Is your Mobishaala OTP for App Login.")

async def send_sms(number, msg):
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest"
    params = {
        "method": "SendMessage",
        "send_to": number,
        # "msg": f"{otp} is your One Time Password (OTP) for Mobishaala, as requested. Thank you for verifying your phone number.",
        "msg": msg,
        "msg_type": "TEXT",
        "userid": "2000177406",
        "auth_scheme": "plain",
        "password": "Mobishaala@2021",
        "v": "1.1",
        "format": "text",
        "principalEntityId": "1201159083037300834",
        # "principalEntityId": "1207169241164878102",
        "mask": "MOBISL",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            logger.info(f"SMS Response: {response.text}")
            response_text = await response.text()
            r_list = response_text.split(' | ')
            return r_list[0] == 'success'
