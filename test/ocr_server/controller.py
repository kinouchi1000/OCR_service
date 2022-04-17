import pytest
import base64

from test.ocr_server._path import *
from src.ocr_server.controller import Controller


@pytest.mark.parametrize(
    "image_path", [("test/data/test.tiff"), ("test/data/test.png")]
)
def test_controller(image_path):
    controller = Controller()

    encode_filename = image_path
    with open(encode_filename, "rb") as f:
        data = f.read()
    encode = base64.b64encode(data)

    print(controller.image_sync(encode))
