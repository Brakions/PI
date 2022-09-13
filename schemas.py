from pydantic import BaseModel
from typing import Optional

class UsersRequestModel(BaseModel):
    username: str
    email : str

class UsersResponseModel(UsersRequestModel):
    id:int