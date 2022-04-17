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
    def get_text(id: uuid.UUID) -> OCRResult:
        """get text from id"""
        with session_scope() as session:
            obj: OCRResult = session.query(OCRResult).filter(OCRResult.id == id).first()
            return obj.to_obj()

    @staticmethod
    def create_result() -> OCRResult:
        """create set text column"""
        with session_scope() as session:
            id: uuid.UUID = uuid.uuid4()
            ocr_result = OCRResult(id=str(id))
            session.add(ocr_result)

            return ocr_result.to_obj()

    @staticmethod
    def update_result(id: str, text: str, image_path: str) -> OCRResult:
        """update result column"""
        with session_scope() as session:
            obj: OCRResult = session.query(OCRResult).filter(OCRResult.id == id).first()
            if obj:
                obj.text = text
                obj.image_path = image_path
