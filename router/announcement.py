from fastapi import APIRouter, Request
from pydantic import BaseModel
from .universal import UserDict
from typing import Optional, Literal, List

# import variables

announcement_router = APIRouter()


class AnnouncementPiece(BaseModel):
    id: int
    publisher_name: str
    time: str
    content: str


@announcement_router.get('/announcement', response_model=List[AnnouncementPiece])
def announcement_lookup(page: int, ann_type: Optional[Literal["user"], Literal["sys"]]):
    return [{'id': 1, 'publisher_name': 'neboer', 'time': "Sun, 19 Jul 2020 06:16:39 GMT", "content": 'happy with me'}]


@announcement_router.get('/announcement/total')
def announcement_total():
    return {'total_number': 1, 'total_pages': 1}
