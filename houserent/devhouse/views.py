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

from django.db import IntegrityError



def url_dev(request):
	if request.method == 'POST':
		url_form = UrlForm(request.POST, submit_title='建立')	
		if url_form.is_valid():			
			form = url_form.save()
			return redirect(reverse('url_work', kwargs={'pk': form.pk}))
	else:
		form = UrlForm(submit_title='建立')
	return render(request, 'url_create.html', {'form': form})

"""
try:
except UnboundLocalError:
	return render(request, 'url_repeat.html', {'form': form})
"""

def get_work(request, pk):
	try:
		dev_house = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
		
	head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	res = requests.get(dev_house.dev_url, headers = head)
	soup = BeautifulSoup(res.text, 'lxml')
	#抓取純文字	
	dev_house.dev_name = soup.find("div", {"class":"avatarRight"}).find("i").text
	dev_house.dev_address = soup.find("span", {"class":"addr"}).text
	dev_house.dev_zone = soup.find("div", { "id" : "propNav" }).find_all("a")[3].text
	dev_house.dev_type = soup.find("div", { "id" : "propNav" }).find_all("a")[4].text
	dev_house.dev_source = '591'
	# 591在整層住家有格局，但是在套房就沒有了
	def get_pattern(): 
		try:
			pattern = soup.find("div", {"class" : "detailInfo clearfix"}).find_all("li")[0].text[6:]
			#pattern.replace(" ","")
			return pattern
		except:
			return ''
	dev_house.dev_pattern = get_pattern()
	# 租金
	money = soup.find("div", {"class":"price clearfix"}).text
	dev_house.dev_rent = ''.join([x for x in money if x.isdigit()])
	# 先把資訊存起來
	dev_house.save()

	# 開始要抓取圖片了!!
	filename = dev_house.dev_name+'-'+dev_house.dev_address
	try:
		phone_img = soup.find("div", {"class":"j-phone infoTwo clearfix-new phone-hide"}).find("img")['src'].split('//')[-1]
		img = 'https://'+phone_img
		filename_phone = 'phone-'+filename
		imgraw = requests.get(img, stream=True)

		img_temp = NamedTemporaryFile(delete=True)
		img_temp.write(imgraw.content)
		img_temp.flush()

		dev_house.dev_phone_img.save('%s.png'%(filename_phone),File(img_temp), save=True)
		del imgraw
	except:
		# It's too bad, no idea to raise except...QQ
		dev_house.dev_phone_img = ''
		dev_house.dev_phone = soup.find("div", { "class" : "infoTwo clearfix" }).find("span", {"class" : "num"}).text
		dev_house.save()

	#f = open('%s.png' % (filename_phone), 'wb')
	#dev_house.dev_phone_img=shutil.copyfileobj(imgraw.raw, f)
	#shutil.copyfileobj(imgraw.raw, f)
	#shutil.move()
	#f.close
	
	
	#電話圖片轉文字
	try:
		image = Image.open("media/%s"%(dev_house.dev_phone_img))
		number = pytesseract.image_to_string(image).replace(" ","")
		dev_house.dev_phone = number
		dev_house.save()
	except:
		print("圖片轉成文字失敗了...")
		pass
	#網頁全圖

	return redirect(reverse('url_list', kwargs={'pk': pk}))	

def url_list(request, pk):
	try:
		url = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	return render(request, 'url_list.html', {'url': url})




# 好房網---------------------------------------

def url_dev_good(request):
	if request.method == 'POST':
		url_form = UrlForm(request.POST, submit_title='建立')
		if url_form.is_valid():
			form = url_form.save()
			return redirect(reverse('url_work_good', kwargs={'pk': form.pk}))
	else:
		form = UrlForm(submit_title='建立')
	return render(request, 'good_url_create.html', {'form': form})


def get_work_good(request, pk):
	try:
		dev_house = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	
	head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	res = requests.get(dev_house.dev_url, headers = head)
	soup = BeautifulSoup(res.text, 'lxml')
	#純文字	
	dev_house.dev_address = soup.find("address", {"class":"value addr"}).text.replace("租金行情","")
	dev_house.dev_name = soup.find("span", {"id":"spanAgent"}).text
	
	fix_phone = soup.find("span", {"class":"tel"}).text 
	fix_phone = ''.join([x for x in fix_phone if x.isdigit()])
	fix_phone = fix_phone[:4] + '-' + fix_phone[4:7] + '-' + fix_phone[7:]
	dev_house.dev_phone = fix_phone
	
	money = soup.find("li", {"class":"DataListWrap"}).find_all("span", "num")[0].text
	dev_house.dev_rent = money
	
	
	dev_house.dev_zone = soup.find("a", { "ga_label" : "detail_breadcrumbs_area" }).text
	dev_house.dev_type =  soup.find_all("span", "value")[7].text
	pattern = soup.find_all("span", "value")[5].text
	dev_house.dev_pattern = pattern.replace("(室)","")
	dev_house.dev_source = '好房網'
	

	dev_house.save()	

	return redirect(reverse('url_list_good', kwargs={'pk': pk}))	

def url_list_good(request, pk):
	try:
		url = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	return render(request, 'good_url_list.html', {'url': url})




# 信義房屋---------------------------------------

def url_dev_sinyi(request):
	if request.method == 'POST':
		url_form = UrlForm(request.POST, submit_title='建立')
		if url_form.is_valid():
			form = url_form.save()
			return redirect(reverse('url_work_sinyi', kwargs={'pk': form.pk}))
	else:
		form = UrlForm(submit_title='建立')
	return render(request, 'sinyi_url_create.html', {'form': form})


def get_work_sinyi(request, pk):
	try:
		dev_house = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	
	head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	res = requests.get(dev_house.dev_url, headers = head)
	soup = BeautifulSoup(res.text, 'lxml')
	#純文字	
	
	dev_house.dev_name = soup.find("div", {"class":"landlord"}).text
	
	# 因為電話是用class包起來，所以要分析有點麻煩
	#fix_phone = soup.find("span", {"class":"tel"}).text 
	#fix_phone = ''.join([x for x in fix_phone if x.isdigit()])
	#fix_phone = fix_phone[:4] + '-' + fix_phone[4:7] + '-' + fix_phone[7:]
	#dev_house.dev_phone = fix_phone
	
	#區域
	#dev_house.dev_zone = soup.find("a", { "ga_label" : "detail_breadcrumbs_area" }).text
	#地址
	dev_house.dev_address = soup.find("section", {"class":"infoTable"}).find_all('td')[0].text
	#租金
	money = soup.find("section", {"class":"infoTable"}).find_all('td')[1].text
	dev_house.dev_rent = ''.join([x for x in money if x.isdigit()])
	#類型
	dev_house.dev_type = soup.find("section", {"class":"infoTable"}).find_all('td')[2].text
	#格局
	dev_house.dev_pattern =  soup.find("section", {"class":"infoTable"}).find_all('td')[3].text
	
	dev_house.dev_source = '信義房屋'
	

	dev_house.save()	

	return redirect(reverse('url_list_sinyi', kwargs={'pk': pk}))	

def url_list_sinyi(request, pk):
	try:
		url = Devinfo.objects.get(pk=pk)
	except Devinfo.DoesNotExist:
		raise Http404
	return render(request, 'sinyi_url_list.html', {'url': url})

