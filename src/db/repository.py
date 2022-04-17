from os import stat
import uuid
from typing import Optional, List

from sqlalchemy.sql.functions import user
from sqlalchemy import desc

from db.setting import session_scope
from db.tables import OCRResult


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
    def create_text(text: str, image_path: str) -> OCRResult:
        """create set text column"""
        with session_scope() as session:
            ocr_result = OCRResult(text=text, image_path=image_path)
            session.add(ocr_result)
            return ocr_result
