from devhouse.models import Devinfo

from django.core.files import File
from PIL import Image
#from django.core.files.temp import NamedTemporaryFile
#import requests

from pyvirtualdisplay import Display
from selenium import webdriver



with Display():
	#Browser = webdriver.Chrome(executable_path='/Users/tsujitoe-mac/program/Python/houserent/houserent/static/browser/chromedriver_mac')
	Browser = webdriver.Firefox()

	# 截圖-----------------
	try:
		infos = Devinfo.objects.all()
		for info in infos:
			if info.dev_screenshot_yes == False:
				get_591 = info.dev_url
				Browser.get(get_591)
				Browser.save_screenshot('screen.png')
				#filename_screen = 'screen-'+info.dev_address
				#img_temp = open('screen.png', 'rb')

				#info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
				info.dev_screenshot_yes = True
				info.save()
				#print('截圖-%s' % info.dev_address)
	

				# 縮圖----------------
				try:
					im = Image.open('screen.png')
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

			else:
				print('這個網址已經截圖過了-%s' % info.dev_address)
	finally:
		Browser.quit()



"""
# pythonanywhere 沒辦法使用 phantomJS
driver = webdriver.PhantomJS(executable_path='/Users/tsujitoe-mac/program/Python/houserent/houserent/static/node_modules/phantomjs/bin/phantomjs') # or add to your PATH
driver.set_window_size(1024, 768) # optional

infos = Devinfo.objects.all()
for info in infos:
	get_591=info.dev_url
	driver.get(get_591)
	driver.save_screenshot('screen.png')

	filename_screen = 'screen-'+info.dev_address

	img_temp = open('screen.png', 'rb')

	#img_temp = NamedTemporaryFile(delete=True)
	#img_temp.write(imgraw)
	#img_temp.flush()

	info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
	print('已經截圖了-%s' % info.dev_address)
"""



"""
# 使用django-screamhot
# 這個api背後還是PhantomJS

#host_url="http://tsujitoe.pythonanywhere.com"
host_url="http://127.0.0.1:8000"

infos = Devinfo.objects.all()
for info in infos:
	#if info.dev_screenshot_img is None:
	try:
		get_591=info.dev_url
		img = "%s/capture/?url=%s&selector=body&width=1100&height=100&size=800x800" % (host_url,get_591)
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
	#else:
	#	print('已經截圖了')
	#	print('%s'%info.id)
"""


"""
# 使用網路上的api，不過是失敗的
apiKey = "OwTxz6SgUOK1n2w0"
agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

infos = Devinfo.objects.all()
for info in infos:
	get_591=info.dev_url
	img='https://api.urlbox.io/v1/%s/png?url=%s&user_agent=%s&timeout=30000'%(apiKey,get_591,agent)
	filename_screen = 'screen-'+info.dev_address
	imgraw = requests.get(img, stream=True)

	img_temp = NamedTemporaryFile(delete=True)
	img_temp.write(imgraw.content)
	img_temp.flush()
	info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
	print("ok--%s"%(filename_screen))
	#except:
	print('這連結有問題-%s'%info.dev_url)
	print('沒有圖片')
	pass
	#else:
	#	print('已經截圖了')
	#	print('%s'%info.id)
"""






"""
import imgkit
options = {
	'format': 'png',
	'crop-h': '900',
	'crop-w': '1300',
	'crop-x': '3',
	'crop-y': '3',
	'encoding': "UTF-8",
	'custom-header' : {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'},
	'no-outline': None,
	'quiet': '',
}

#infos = Devinfo.objects.all()
#for info in infos:
#if infos.dev_screenshot_img is None:
infos = Devinfo.objects.all()
for info in infos:
	get_591=info.dev_url
	imgkit.from_url(get_591, '%s.png'%info.dev_address, options=options)
	print("ok--%s"%(info.id))
			#filename_screen = 'screen-'+info.dev_address
			#imgraw = requests.get(img, stream=True)

			#img_temp = NamedTemporaryFile(delete=True)
			#img_temp.write(imgraw.content)
			#img_temp.flush()

			#info.dev_screenshot_img.save('%s.png'%(filename_screen),File(img_temp), save=True)
"""



# 使用api
"""
from urllib.parse import urlencode
from urllib.request import urlretrieve

params = urlencode({"url": "http://google.com", "access_key": "65ecfae2195744f4aa3ae6c09108d3a2"})
urlretrieve("https://apileap.com/api/screenshot/v1/urltoimage?" + params, "screenshot.jpeg")
"""


# 使用selenium
"""
from devhouse.models import Devinfo
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/Users/tsujitoe-mac/program/Python/houserent/houserent/static/node_modules/phantomjs/bin/phantomjs')
infos = Devinfo.objects.all()
for info in infos:
	if info.dev_screenshot_img is None:
		try:
			driver.get(info.dev_url)
			driver.save_screenshot('591%s.png'%(info.dev_address))

			screenshot = driver.screenshot_as_base64() 
			info.dev_screenshot_img = ContentFile(screenshot, '591%s.png'%(info.dev_address))
			info.save()
		except:
			print(info.dev_address)
			print('哪邊有錯誤...QQ')
"""
