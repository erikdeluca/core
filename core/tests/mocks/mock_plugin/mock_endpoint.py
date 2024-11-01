from fastapi import Request, Depends
from pydantic import BaseModel

from cat.mad_hatter.decorators import endpoint, get_endpoint, post_endpoint
from cat.auth.connection import HTTPAuth
from cat.auth.permissions import AuthPermission, AuthResource

class Item(BaseModel):
    name: str
    description: str

@endpoint(path="/endpoint", methods=["GET"], tags=["Tests"])
def test_endpoint():
    return {"result":"endpoint default prefix"}

@endpoint(path="/endpoint", prefix="/tests", methods=["GET"], tags=["Tests"])
def test_endpoint_prefix():
    return {"result":"endpoint prefix tests"}

@get_endpoint(path="/get", prefix="/tests", tags=["Tests"])
def test_get(request: Request, stray=Depends(HTTPAuth(AuthResource.PLUGINS, AuthPermission.LIST))):
    return {"result":"ok", "stray_user_id":stray.user_id}

@post_endpoint(path="/post", prefix="/tests", tags=["Tests"])
def test_post(item: Item) -> str:
    return {"name": item.name, "description": item.description}