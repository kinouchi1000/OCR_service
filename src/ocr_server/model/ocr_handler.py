import os
from PIL import Image
import pyocr
 
#pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]
 
#OCR対象の画像ファイルを読み込む
img = Image.open("test.png")
 
#画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="eng", builder=builder)
 
print(text)