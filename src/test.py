from ocr_server.controller import Controller
import base64

controller = Controller()
encode_filename = "../test/data/test.tiff"
with open(encode_filename, "rb") as f:
    data = f.read()
encode = base64.b64encode(data)
print(controller.image_sync(encode))
