from devhouse.models import Devinfo

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests

host_url="http://tsujitoe.pythonanywhere.com"
#host_url="http://127.0.0.1:8000"

infos = Devinfo.objects.all()
for info in infos:
	if info.dev_screenshot_img is None:
		try:
			get_591=info.dev_url
			img = "%s/capture/?url=%s&selector=bodywidth=1300&height=500&size=1000x1000" % (host_url,get_591)
			filename_screen = 'screen-'+info.dev_address
			imgraw = requests.get(img, stream=True)

			img_temp = NamedTemporaryFile(delete=True)
			img_temp.write(imgraw.content)
			img_temp.flush()

			info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
			print("ok--%s"%(filename_screen))
		except:
			print('這連結有問題-%s'%info.dev_url)
			print('沒有圖片')
			pass
