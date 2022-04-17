import asyncio
from concurrent.futures import ThreadPoolExecutor
import grpc
import logging

from common.constants import OCR_IP, OCR_PORT
from grpc_service import ocr_server_pb2_grpc, ocr_server_pb2
from grpc_service.ocr_server_pb2 import Text, Image, StoreImageParam, Empty

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
        logging.info("image_sync")

        request = Image(data=image)
        feature: Text = self.stub.ImageSync(request)

        return feature.text

    def store_image(self, image: bytes, id: str):

        logging.info("store_image")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
        request = StoreImageParam(data=image, id=id)
        loop.run_in_executor(None, self.stub.StoreImage, request)
        logging.info("finish store image")
