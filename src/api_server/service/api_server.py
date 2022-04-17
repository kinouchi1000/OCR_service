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
    task_id: str


@app.post("/image-sync")
def read_root(image: Image):
    text = controller.image_sync(image.image_data)
    return {"text": text}


@app.post("/image")
def read_item(image: Image):
    id = controller.store_image(image.image_data)
    return {"task_id": id}


@app.get("/image")
def read_item(id: Id):
    text = controller.get_text(id.task_id)
    return {"task_id": text}
