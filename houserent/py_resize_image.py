from devhouse.models import Devinfo

from PIL import Image
from django.core.files import File


infos = Devinfo.objects.all()
for info in infos:
	try:
		im = Image.open(info.dev_screenshot_img)
		#print (im.format, im.size, im.mode)
		if im.size != 600:
			width = 600
			ratio = float(width)/im.size [0]
			height = int(im.size [1] * ratio)

			nim = im.resize((width, height), Image.BILINEAR)
			nim.save('resize.png')
			img_temp = open('resize.png', 'rb')

			filename_screen = 'resize-'+info.dev_address

			info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
	
			info.save()
			print("縮圖ok-%s"%(info.dev_address))
	except:
		print("哪邊有問題?-%s"%(info.dev_address))