#图片识别

#Tesseract的Windows安装包下载地址为：http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe ，
#下载后双击直接安装即可。安装完后，需要将Tesseract添加到系统变量中。在CMD中输入tesseract -v, 
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('E://figures/other/poems.jpg'))

print(text)





