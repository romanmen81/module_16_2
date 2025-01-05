from fastapi import FastAPI, Path
from pydantic import constr, conint
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[conint(ge=1, le=100), Path(title="User ID", description="Enter User ID", example=1)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[constr(min_length=5, max_length=20), Path(title="Username", description="Enter username", example="UrbanUser")],
    age: Annotated[conint(ge=18, le=120), Path(title="Age", description="Enter age", example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
