from PIL import Image
import pyocr


class OCRHandler:
    def __init__(self):
        pass

    def get_ocr_text(self, file_name: str) -> str:
        """make OCR and get text
        Args:
            file_name(str): image written text
        """
        # pyocrへ利用するOCRエンジンをTesseractに指定する。
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # OCR対象の画像ファイルを読み込む
        img = Image.open(file_name)

        # 画像から文字を読み込む
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        text = tool.image_to_string(img, lang="eng", builder=builder)

        return text


if __name__ == "__main__":

    ocr_handler = OCRHandler()
    text = ocr_handler.get_ocr_text("test/data/text.png")
    print(text)
