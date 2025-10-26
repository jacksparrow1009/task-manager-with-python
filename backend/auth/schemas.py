from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: constr(min_length=6, max_length=72) # type: ignore

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=72) # type: ignore

class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str
    created_at: str

    class Config:
        from_attributes = True