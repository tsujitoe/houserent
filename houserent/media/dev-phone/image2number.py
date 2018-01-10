import pytesseract
from PIL import Image

image = Image.open('phone-可伊-台中市北屯區文心路四段.png') #圖檔名稱
number = pytesseract.image_to_string(image)
print ("The captcha is:%s" % number)
