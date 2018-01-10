from django.shortcuts import render
from django.core.urlresolvers import reverse #Django1.8.8

from .models import Devinfo
from .forms import UrlForm

from django.shortcuts import render, redirect
from django.http import HttpResponse

from bs4 import BeautifulSoup
#from selenium import webdriver
import requests
#import shutil

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import pytesseract
from PIL import Image



def url_dev(request):
	if request.method == 'POST':
		url_form = UrlForm(request.POST, submit_title='建立')
		if url_form.is_valid():
			form = url_form.save()
			return redirect(reverse('url_work', kwargs={'pk': form.pk}))
	else:
		form = UrlForm(submit_title='建立')
	return render(request, 'url_create.html', {'form': form})



from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


import pytesseract
from PIL import Image



def get_work(request, pk):
	try:
		dev_house = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404

	head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	res = requests.get(dev_house.dev_url, headers = head)
	soup = BeautifulSoup(res.text, 'lxml')
	#純文字
	dev_house.dev_name = soup.find("div", {"class":"avatarRight"}).find("i").text
	dev_house.dev_address = soup.find("span", {"class":"addr"}).text
	dev_house.dev_zone = soup.find("div", { "id" : "propNav" }).find_all("a")[3].text
	
	money = soup.find("div", {"class":"price clearfix"}).text
	dev_house.dev_rent = ''.join([x for x in money if x.isdigit()])
	
	dev_house.save()

	filename = dev_house.dev_name+'-'+dev_house.dev_address
	#電話圖片
	phone_img = soup.find("div", {"class":"infoTwo clearfix"}).find("img")['src'].split('//')[-1]
	img = 'https://'+phone_img
	filename_phone = 'phone-'+filename
	imgraw = requests.get(img, stream=True)
	
	img_temp = NamedTemporaryFile(delete=True)
	img_temp.write(imgraw.content)
	img_temp.flush()

	dev_house.dev_phone_img.save('%s.png'%(filename_phone),File(img_temp), save=True)
	#f = open('%s.png' % (filename_phone), 'wb')
	#dev_house.dev_phone_img=shutil.copyfileobj(imgraw.raw, f)
	#shutil.copyfileobj(imgraw.raw, f)
	#shutil.move()
	#f.close
	del imgraw
	
	#電話圖片轉文字
	image = Image.open("media/%s"%(dev_house.dev_phone_img))
	number = pytesseract.image_to_string(image).replace(" ","")
	dev_house.dev_phone = number

	dev_house.save()

	#網頁全圖

	return redirect(reverse('url_list', kwargs={'pk': pk}))


def url_list(request, pk):
	try:
		url = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	return render(request, 'url_list.html', {'url': url})



