import pytest
import pathlib
from test.ocr_server._path import *

from src.ocr_server.model.ocr_handler import OCRHandler


@pytest.mark.parametrize(
    "image_path", [("test/data/test.tiff"), ("test/data/test.png")]
)
def test_get_ocr_text(image_path):
    ocr_handler = OCRHandler()
    image_path = pathlib.Path(image_path)
    text = ocr_handler.get_ocr_text(image_path)
    assert text == "Challenge to make OCR!!!"
