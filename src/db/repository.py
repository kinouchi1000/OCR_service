from os import stat
import uuid
import pathlib
from typing import Optional, List

from sqlalchemy.sql.functions import user
from sqlalchemy import desc

from db.setting import session_scope
from db.tables import OCRResult
from common.constants import IMAGE_DIR


class Repository:
    """
    CRUD for OCRResult
    """

    @staticmethod
    def get_text(id: uuid.UUID) -> List[OCRResult]:
        """get text from id"""
        with session_scope() as session:
            obj = session.query(OCRResult).filter(OCRResult.id == id).all()
            return list(map(lambda x: x.to_obj(), obj))

    @staticmethod
    def create_text(text: str, extention: str) -> OCRResult:
        """create set text column"""
        with session_scope() as session:
            id: uuid.UUID = uuid.uuid4()
            image_path = pathlib.Path(IMAGE_DIR) / (str(id) + extention)
            ocr_result = OCRResult(id=str(id), text=text, image_path=str(image_path))
            session.add(ocr_result)

            return ocr_result.to_obj()
