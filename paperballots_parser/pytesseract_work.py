from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
img = Image.open('./samples/first_page.jpg')
print(pytesseract.image_to_string(img, lang="fra"))