import asyncio
from api_server.service.ocr_client import OCRClient
from db.repository import Repository


class Controller:
    def __init__(self) -> None:
        self.ocr_client = OCRClient()
        self.repository = Repository()

    def image_sync(self, image_data: bytes) -> str:
        text = self.ocr_client.image_sync(image=image_data)
        return text

    def store_image(self, image_data: bytes) -> int:

        ocr_result = self.repository.create_result()
        asyncio.run(self.ocr_client.store_image(image=image_data, id=ocr_result.id))
        return ocr_result.id

    def get_text(self, id: str) -> str:
        ocr_result = self.repository.get_text(id)
        return ocr_result.text
