from fastapi import APIRouter, File, UploadFile
from typing import List
import shutil
from pydantic import BaseModel, EmailStr, validator


class QueryModel(BaseModel):
    query: str


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'username must be alphanumeric'
        return v


router = APIRouter()


@router.get("/")
async def index():
    return {"status": "ok"}


@router.post("/signup")
async def create_user(user: UserModel):
    return user


@router.post("/upload")
def upload_document(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            with open("documents/" + file.filename, 'wb') as f:
                shutil.copyfileobj(file.file, f)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}


@router.post("/search")
async def search_document(query: QueryModel):
    return query
