from api_server.service.ocr_client import OCRClient


class Controller:
    def __init__(self) -> None:
        self.ocr_client = OCRClient()

    def image_sync(self, image_data: bytes) -> str:
        text = self.ocr_client.image_sync(image=image_data)
        return text

    def store_image(self, image_data: bytes):
        pass

    def get_text(self, id: str):
        pass
