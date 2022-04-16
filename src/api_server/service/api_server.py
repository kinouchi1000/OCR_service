from lib2to3.pytree import Base
from fastapi import FastAPI
from pydantic import BaseModel
from api_server.controller import Controller
import logging


app = FastAPI()

controller = Controller()
logger = logging.getLogger(__name__)


class Image(BaseModel):
    image_data: bytes


class Text(BaseModel):
    text: str


class Id(BaseModel):
    id: str


@app.post("/image-sync")
def read_root(image: Image):
    text = controller.image_sync(image.image_data)
    return {"text": text}


@app.post("/image")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/image")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
