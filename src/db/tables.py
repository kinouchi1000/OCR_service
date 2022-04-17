from dataclasses import dataclass, field
from email.policy import default
import uuid
import datetime
from typing import Optional


from sqlalchemy import DATETIME, Column, Integer, String, DateTime, Table

from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import registry, relationship, backref

from db.setting import ENGINE


mapper_registy = registry()


@mapper_registy.mapped
@dataclass
class OCRResult:
    """
    OCR result DB
    """

    __table__ = Table(
        "ocr_result",
        mapper_registy.metadata,
        Column("id", UUIDType(binary=False), primary_key=True, default=uuid.uuid4),
        Column("text", String(256)),
        Column("image_path", String(256)),
        Column("date_time", DATETIME, server_default=func.now(), onupdate=func.now()),
    )
    id: uuid.UUID = None
    text: str = None
    image_path: str = None
    date_time: Optional[datetime.datetime] = None

    def to_obj(self):
        ocr_result = OCRResult()
        ocr_result.id = self.id
        ocr_result.text = self.text
        ocr_result.image_path = self.image_path
        ocr_result.date_time = self.date_time

        return ocr_result


def init_db():
    mapper_registy.metadata.create_all(bind=ENGINE)
