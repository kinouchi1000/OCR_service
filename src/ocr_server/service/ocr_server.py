from concurrent import futures
import grpc
import logging

from grpc_service import ocr_server_pb2_grpc, ocr_server_pb2
from common.constants import OCR_IP, OCR_PORT, MAX_WORKERS
from ocr_server.controller import Controller

logger = logging.getLogger(__name__)


class OCRServicer(ocr_server_pb2_grpc.OCRServerServicer):
    def __init__(self) -> None:
        self.controller = Controller()

    def ImageSync(self, request, context):

        logger.info("called Image sync")
        image: bytes = request.data
        text = self.controller.image_sync(image=image)
        ret = ocr_server_pb2.Text(text=text)

        return ret

    def StoreImage(self, request, context):
        logger.info("StoreImage is called")

        task_id: str = request.id
        image: bytes = request.data
        self.controller.store_image(image=image, id=task_id)
        ret = ocr_server_pb2.Empty(status_code=0)

        return ret

    # def GetText(self, request, context):
    #     logger.info("GetText is called")

    #     task_id: str = request.id
    #     # TODO not implemented
    #     return super().GetText(request, context)


def servier():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    ocr_server_pb2_grpc.add_OCRServerServicer_to_server(OCRServicer(), server)
    server.add_insecure_port(f"[::]:{OCR_PORT}")
    server.start()
    server.wait_for_termination()
