import cv2
import base64
import numpy as np
import imghdr
import sys
import pathlib


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def save_image_from_base64(
        image_data: bytes, store_path: pathlib.Path, id: str
    ) -> pathlib.Path:
        """convert image from base64 bytes data.
        It detect extention (.png .tiff) automaticaly
        """

        # convert to binary data
        img_binary = base64.b64decode(image_data)

        # extention judgment
        imagetype = imghdr.what(None, h=img_binary)
        if imagetype is None:
            sys.stderr.write("Can't detect extention from binary")
        _img = np.frombuffer(img_binary, dtype=np.uint8)

        # raw image
        img = cv2.imdecode(_img, cv2.IMREAD_COLOR)

        # save
        file_name: str = id + "." + imagetype
        file_path = store_path / file_name
        cv2.imwrite(str(file_path), img)

        return file_path
