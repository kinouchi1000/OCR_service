import grpc
import logging

from common.constants import OCR_IP, OCR_PORT
from grpc_service import ocr_server_pb2_grpc, ocr_server_pb2
from grpc_service.ocr_server_pb2 import Text, Image, Id

logger = logging.getLogger(__name__)


class OCRClient:
    def __init__(self) -> None:
        self._channel = None
        self.stub = None

        self._channel = grpc.insecure_channel(f"{OCR_IP}:{OCR_PORT}")
        self.stub = ocr_server_pb2_grpc.OCRServerStub(channel=self._channel)

    def __del__(self):
        if self._channel:
            self._channel.close()

    def image_sync(self, image: bytes) -> str:
        logger.info(f"image: {type(image)}")

        ret = Image(data=image)
        feature: str = self.stub.ImageSync(ret)

        return feature.text

    def store_image(self) -> None:
        # TODO must implement
        pass

    def get_text(self) -> None:
        # TODO must implement
        pass
