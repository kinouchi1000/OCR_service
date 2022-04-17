import base64

import base64
import requests
from pydantic import BaseModel


class Image(BaseModel):
    image_data: bytes


class Text(BaseModel):
    text: str


class Id(BaseModel):
    id: str


def test_image_sync():

    encode_filename = "test/data/test.png"
    with open(encode_filename, "rb") as f:
        data = f.read()
    image_data = base64.b64encode(data)
    image = Image(image_data=image_data)

    url = "http://127.0.0.1:5000/image-sync/"
    r = requests.post(url, data=image.json())
    print(r)
    result = r.json()
    return result


print(test_image_sync())