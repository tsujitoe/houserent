from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.forms.models import inlineformset_factory

from .models import MediaInfo, Media, FakeInfo
from .forms import MediaInfoForm, MediaForm, MediaInlineFormset, UrlForm
#from .models import Post, Images_street
#from .forms import PostForm, ImageForm, ImageFormSet


from bs4 import BeautifulSoup
#from selenium import webdriver
import requests
#import shutil

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import pytesseract
from PIL import Image


# Create your views here.

def street_create(request):
	if request.method == 'POST':
		form = MediaInfoForm(request.POST, submit_title='建立')
		if form.is_valid():
			title_address = form.save(commit=False)
			title_address.save()
			return redirect(title_address.get_absolute_url())
	else:
		form = MediaInfoForm(submit_title='建立')
	return render(request, 'street_create.html', {'form': form})


def street_update(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk) 
	except MediaInfo.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		form = MediaInfoForm(request.POST, instance=address, submit_title=None)
		formset = MediaInlineFormset(request.POST, request.FILES, instance=address)
		if form.is_valid() and formset.is_valid():
			address = form.save()
			formset.save()
			return redirect(address.get_absolute_url())
	else:
		form = MediaInfoForm(instance=address, submit_title=None)
		form.helper.form_tag = False
		formset = MediaInlineFormset(instance=address)
	return render(request, 'street_update.html', {'form': form, 'formset': formset, 'address': address })


def  street_detail(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk)
	except MediaInfo.DoesNotExist:
		raise Http404
	return render(request, 'street_detail.html', {'address': address})


def street_mul_image(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk)
	except MediaInfo.DoesNotExist:
		raise Http404
	if request.method == "POST":
		formset = MediaInlineFormset(request.POST, request.FILES, instance=address)
		if formset.is_valid():
			formset.save()
			return redirect(address.get_absolute_url())
	else:
		formset = MediaInlineFormset(instance=address)
	return render(request, 'street_mul_image.html', {'address':address, 'formset':formset})



def street_image(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk)
	except MediaInfo.DoesNotExist:
		raise Http404
	if request.method == "POST":
		form = MediaInlineFormset(request.POST, request.FILES, instance=address)
		if form.is_valid():
			form.save()
			return redirect(address.get_absolute_url())
	else:
		form = MediaInlineFormset(instance=address)
	return render(request, 'street_image.html', {'address':address, 'form':form})



# for fake tenant
# just for 591

def url_dev(request):
	if request.method == 'POST':
		url_form = UrlForm(request.POST, submit_title='建立')
		if url_form.is_valid():
			form = url_form.save()
			return redirect(reverse('url_work_fake', kwargs={'pk': form.pk}))
	else:
		form = UrlForm(submit_title='建立')
	return render(request, 'fake_url_create.html', {'form': form})

"""
try:
except UnboundLocalError:
	return render(request, 'url_repeat.html')
"""

def get_work(request, pk):
	try:
		fake_house = FakeInfo.objects.get(pk=pk)
	except FakeInfo.DoesNotExist:
		raise Http404
	
	head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	res = requests.get(fake_house.fake_url, headers = head)
	soup = BeautifulSoup(res.text, 'lxml')
	#純文字	
	fake_house.fake_name = soup.find("div", {"class":"avatarRight"}).find("i").text
	fake_house.fake_address = soup.find("span", {"class":"addr"}).text
	fake_house.fake_zone = soup.find("div", { "id" : "propNav" }).find_all("a")[3].text
	fake_house.fake_type = soup.find("div", { "id" : "propNav" }).find_all("a")[4].text
	

	money = soup.find("div", {"class":"price clearfix"}).text
	fake_house.fake_rent = ''.join([x for x in money if x.isdigit()])

	fake_house.fake_source = '591'

	fake_house.save()

	filename = fake_house.fake_name+'-'+fake_house.fake_address
	#電話圖片
	phone_img = soup.find("div", {"class":"infoTwo clearfix"}).find("img")['src'].split('//')[-1]
	img = 'https://'+phone_img
	filename_phone = 'phone-'+filename
	imgraw = requests.get(img, stream=True)

	img_temp = NamedTemporaryFile(delete=True)
	img_temp.write(imgraw.content)
	img_temp.flush()

	fake_house.fake_phone_img.save('%s.png'%(filename_phone),File(img_temp), save=True)
	#f = open('%s.png' % (filename_phone), 'wb')
	#dev_house.dev_phone_img=shutil.copyfileobj(imgraw.raw, f)
	#shutil.copyfileobj(imgraw.raw, f)
	#shutil.move()
	#f.close
	del imgraw
	
	return redirect(reverse('url_list_fake', kwargs={'pk': pk}))	

def url_list(request, pk):
	try:
		url = FakeInfo.objects.get(pk=pk)
	except FakeInfo.DoesNotExist:
		raise Http404
	return render(request, 'fake_url_list.html', {'url': url})





"""
#for multi upload image

			for count, x in enumerate(request.FILES.getlist("image"))
				def handle_uploaded_file(f):
				with open('some/file/name.txt', 'wb+') as destination:
					for chunk in f.chunks():
						destination.write(chunk)
				process(x)
"""


"""
def post(request):
	if request.method == 'POST':
		postForm = PostForm(request.POST, submit_title='上傳')
		formset = ImageFormSet(request.POST, request.FILES, queryset=Images_street.objects.none())
		if postForm.is_valid() and formset.is_valid():
			post_form = postForm.save(commit=False)
			post_form.save()

			for form in formset.cleaned_data:
				image = form['image']
				photo = Images_street(post=post_form)
				photo.save()
			#messages.success(request, "Yeeew,check it out on the home page!")
			return HttpResponseRedirect("/")
		else:
			print(postForm.errors)
			print(formset.errors)
	else:
		postForm = PostForm()
		formset = ImageFormSet(queryset=Images_street.objects.none(), submit_title='上傳')
	return render(request, 'gostreet.html',
		{'postForm': postForm, 'formset': formset}, )
"""


