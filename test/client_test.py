import base64

import base64
import requests
from pydantic import BaseModel
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("mode", help="select from [image-sync, post-image, get-image]")
parser.add_argument(
    "--image-path", help="default is test/data/test.png", default="test/data/test.png"
)
parser.add_argument("--id", help="if you use get_image, please set id")
args = parser.parse_args()


class Image(BaseModel):
    image_data: bytes


class Text(BaseModel):
    text: str


class Id(BaseModel):
    task_id: str


class ClientTest:
    @staticmethod
    def test_image_sync(encode_filename: str):

        with open(encode_filename, "rb") as f:
            data = f.read()
        image_data = base64.b64encode(data)
        image = Image(image_data=image_data)

        url = "http://127.0.0.1:5000/image-sync/"
        r = requests.post(url, data=image.json())
        print(r)
        result = r.json()
        return result

    @staticmethod
    def test_post_image(encode_filename: str):
        with open(encode_filename, "rb") as f:
            data = f.read()
        image_data = base64.b64encode(data)

        image = Image(image_data=image_data)

        url = "http://127.0.0.1:5000/image/"
        r = requests.post(url, data=image.json())
        print(r)
        result = r.json()
        return result

    @staticmethod
    def test_get_image(task_id: str):

        id_param = Id(task_id=task_id)

        url = "http://127.0.0.1:5000/image/"
        r = requests.get(url, data=id_param.json())
        print(r)
        result = r.json()
        return result


if __name__ == "__main__":
    if args.mode == "image-sync":
        if not args.image_path:
            print("Please set image path with --image-path")
            sys.exit(0)
        result = ClientTest.test_image_sync(args.image_path)
        print(result)

    elif args.mode == "post-image":
        if not args.image_path:
            print("Please set image path with --image-path")
            sys.exit(0)
        task_id = ClientTest.test_post_image(args.image_path)
        print(task_id)

    elif args.mode == "get-image":
        if not args.id:
            print("Please set id with --id")
            sys.exit(0)
        test = ClientTest.test_get_image(task_id=args.id)
        print(test)

    else:
        print("Please set mode ")
