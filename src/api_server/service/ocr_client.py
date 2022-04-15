import grpc

from common.constants import OCR_IP, OCR_PORT


class OCRClient:
    def __init__(self) -> None:
        self._channel = None
        self.stub = None

        self._channel = grpc.insecure_channel(f"{OCR_IP}:{OCR_PORT}")

    def __del__(self):
        if self._channel:
            self._channel.close()

    def image_sync(self) -> None:
        # TODO must implement
        pass

    def store_image(self) -> None:
        # TODO must implement
        pass

    def get_text(self) -> None:
        # TODO must implement
        pass
