from fastapi import APIRouter, Request
from pydantic import BaseModel
from .universal import UserDict

# import variables

user_router = APIRouter()


class UserLogin(BaseModel):
    username: str
    password: str


@user_router.post("/login")
def temp_login_with_password(user: UserLogin, request: Request):
    if user.username == "user" and user.password == "pass":
        request.session['user'] = {'id': 1234, 'privilege': 1, 'username': user.username}
        return {'result': 'successful', 'privilege': 1}
    elif user.username == 'admin' and user.password == 'pass':
        request.session['user'] = {'id': 1235, 'privilege': 2, 'username': user.username}
        return {'result': 'successful', 'privilege': 2}
    elif user.username == 'op' and user.password == 'pass':
        request.session['user'] = {'id': 1236, 'privilege': 3, 'username': user.username}
        return {'result': 'successful', 'privilege': 3}
    else:
        return {'result': 'failed'}


@user_router.get("/login")
def temp_login_with_cookies(request: Request):
    if request.session == {}:
        return {'result': 'failed'}
    else:
        request_user: UserDict = request.session['user']
        return {'username': request_user['username'], 'privilege': request_user['privilege']}
