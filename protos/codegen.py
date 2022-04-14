from grpc.tools import protoc

path = "./ocr_server.proto"

protoc.main(
    (
        "",
        "-I.",
        "--python_out=../src/grpc_service/",
        "--grpc_python_out=../src/grpc_service/",
        f"./{path}",
    )
)
