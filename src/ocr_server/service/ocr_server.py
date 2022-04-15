from concurrent import futures
import grpc

from grpc_service import ocr_server_pb2_grpc
from common.constants import OCR_IP, OCR_PORT, MAX_WORKERS
from ocr_server.controller import Controller


class OCRServicer(ocr_server_pb2_grpc.OCRServerServicer):
    def __init__(self) -> None:
        self.controller = Controller

    def ImageSync(self, request, context):
        # TODO not implemented
        return super().ImageSync(request, context)

    def StoreImage(self, request, context):
        # TODO not implemented
        return super().StoreImage(request, context)

    def GetText(self, request, context):
        # TODO not implemented
        return super().GetText(request, context)


def servier():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    ocr_server_pb2_grpc.add_OCRServerServicer_to_server(OCRServicer(), server)
    server.add_insecure_port(f"{OCR_IP}:{OCR_PORT}")
    server.start()
    server.wait_for_termination()
