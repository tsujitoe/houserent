
from devhouse.models import Devinfo
import pytesseract
from PIL import Image

infos = Devinfo.objects.all()
for info in infos:
	if info.dev_phone is None:
		try:
			image = Image.open("media/%s"%(info.dev_phone_img))
			number = pytesseract.image_to_string(image).replace(" ","")
			info.dev_phone = number
			info.save()
		except:
			print(info.dev_address)
			print('沒有圖片')
			pass

