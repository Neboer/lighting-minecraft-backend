from typing import Optional
from fastapi import FastAPI, Request
import variables
from starlette.middleware.sessions import SessionMiddleware
from router.login import user_router

app = FastAPI(debug=True)

app.add_middleware(SessionMiddleware, secret_key=variables.session_secret_key)
app.include_router(user_router, prefix='/api')


@app.get("/")
def read_root(request: Request):
    request.session[variables.session_title] = 'hello'
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, request: Request = None):
    print(request.session)
    return {"item_id": item_id, "q": q}
