from pydantic import BaseModel, constr

class OtpRequest(BaseModel):
    number: constr(min_length=10, max_length=10)

class OtpResponse(BaseModel):
    status: str

__all__ = ["OtpRequest", "OtpResponse"]
