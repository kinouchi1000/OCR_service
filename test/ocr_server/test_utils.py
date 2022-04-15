import pytest
import base64
import pathlib
import cv2
import numpy as np
from test.ocr_server._path import *

from src.ocr_server.model.utils import Utils


@pytest.mark.parametrize(
    "image_path", [("test/data/test.tiff"), ("test/data/test.png")]
)
def test_save_image_from_base64(image_path):
    utls = Utils()

    encode_filename = image_path
    with open(encode_filename, "rb") as f:
        data = f.read()
    encode = base64.b64encode(data)

    decode_path = pathlib.Path("test/")

    save_filename = utls.save_image_from_base64(
        image_data=encode, store_path=decode_path, id="test"
    )

    im1 = cv2.imread(str(encode_filename))
    im2 = cv2.imread(str(save_filename))

    print(np.array_equal(im1, im2))
