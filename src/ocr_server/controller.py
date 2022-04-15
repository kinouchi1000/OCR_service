import logging
import uuid
import base64
import pathlib
import sys

from common.constants import IMAGE_DIR
from ocr_server.model.ocr_handler import OCRHandler
from ocr_server.model.utils import Utils

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self):

        self.ocr_handler = OCRHandler()
        self.utils = Utils()

    def image_sync(self, image: bytes) -> str:
        """this function get encoded image data by base64, and return text,
        Args:
            image(str): image data
        """
        logger.info("start image sync")
        try:
            # decode image
            image_id = str(uuid.uuid1())
            store_dir = pathlib.Path(IMAGE_DIR)
            if not store_dir.exists():
                store_dir.mkdir(parents=True)
            filename = self.utils.save_image_from_base64(image, store_dir, image_id)

            # make OCR
            text = self.ocr_handler.get_ocr_text(file_name=filename)
            # delete image file
            pathlib.Path(filename).unlink()
            return text
        except Exception as e:
            logger.warn(f"error:{e}")
            return None
