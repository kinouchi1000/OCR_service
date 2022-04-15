from PIL import Image
import pyocr
import pathlib
from common.constants import OCR_TESSERACT_LAYER, OCR_LANG


class OCRHandler:
    def __init__(self):
        pass

    def get_ocr_text(self, file_name: pathlib.Path) -> str:
        """make OCR and get text
        Args:
            file_name(str): image written text
        """
        # pyocrへ利用するOCRエンジンをTesseractに指定する。
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # OCR対象の画像ファイルを読み込む
        img = Image.open(str(file_name))

        # 画像から文字を読み込む
        builder = pyocr.builders.TextBuilder(tesseract_layout=OCR_TESSERACT_LAYER)
        text = tool.image_to_string(img, lang=OCR_LANG, builder=builder)

        return text
