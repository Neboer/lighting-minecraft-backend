from fastapi import APIRouter, Request
from pydantic import BaseModel
from .universal import UserDict
from typing import Optional, Literal, List

# import variables

invitation_router = APIRouter()


@invitation_router.get('/invitation')
def invite_code(req: Request):
    request_user: UserDict = req.session['user']
    return {'A2s314': None, '1389po': None, 'asdfggh': {'id': 1234, 'username': 'neboer'}}

