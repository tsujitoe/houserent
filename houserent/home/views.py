
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.files.base import ContentFile
import os.path

from .models import HomeInfo, HomeMediaInfo, HomePhoto
from .forms import HomeInfoForm, HomePhotoForm


def home_info_create(request):
	if request.method == 'POST':
		home_form = HomeInfoForm(request.POST, request.FILES)
		#img_form = HomePhotoForm(request.POST, request.FILES)
		#if home_form.is_valid() and img_form.is_valid():
		if home_form.is_valid():
			# 1 agree
			home_info = HomeInfo.objects.create()
			#基本資料
			home_info.home_address=home_form.cleaned_data['home_address'] 
			home_info.home_master=home_form.cleaned_data['home_master'] 
			home_info.home_master_phone=home_form.cleaned_data['home_master_phone'] 
			home_info.home_how_inter_door=home_form.cleaned_data['home_how_inter_door'] 
			#案件格局
			home_info.home_type=home_form.cleaned_data['home_type']
			home_info.home_square=home_form.cleaned_data['home_square']
			home_info.home_how_manage=home_form.cleaned_data['home_how_manage']  
			home_info.home_garbage=home_form.cleaned_data['home_garbage'] 
			home_info.home_park=home_form.cleaned_data['home_park']
			#租金細目
			home_info.home_rent=home_form.cleaned_data['home_rent'] 
			home_info.home_include=home_form.cleaned_data['home_include'] 
			home_info.home_fee_note=home_form.cleaned_data['home_fee_note'] 
			#設備包含
			home_info.home_equipment=home_form.cleaned_data['home_equipment'] 
			#條件限制
			home_info.home_pet_limit=home_form.cleaned_data['home_pet_limit'] 
			home_info.home_people_limit=home_form.cleaned_data['home_people_limit'] 			
			#補充資訊
			home_info.home_note=home_form.cleaned_data['home_note'] 

			home_info.save()

			"""
			home_address = request.POST.get('address', '')
			home_info = HomeInfo.objects.create(home_address = home_address)
			home_info.save()
			"""
			"""
			# 2 agree
			info_title = request.POST.get('title', '')
			info = HomeMediaInfo.objects.create(home_address=home_info, home_title=info_title)
			info.save()

			# 3 agree
			if 'docfile' in request.FILES:
				image_list = request.FILES.getlist('docfile')
				for a_image in image_list:
					s = HomePhoto(h_title=info, h_image=a_image)
					s.save()
				#return HttpResponse('upload ok!')
			"""
			return redirect(home_info.get_absolute_url())
		else:
			print(home_form.errors)
			return HttpResponse('upload QQ !')
	else:
		home_form = HomeInfoForm()
	return render(request,'upload_image.html', {'home_form': home_form})



def home_info_detail(request, pk):
	try:
		home_info = HomeInfo.objects.get(pk=pk)
	except HomeInfo.DoesNotExist:
		raise Http404
	return render(request, 'home_detail.html', {'home_info': home_info})
"""

  <a href="{% url 'photo_create' pk=home_info.pk %}" class="btn btn-default">新增相簿</a>
  <a href="{% url 'home_info_update' pk=home_info.pk %}" class="btn btn-default">更新案件資訊</a>
"""





def home_info_list(self):
	return HttpResponse('home_info_list')

def home_info_update(request, self):
	return HttpResponse('home_info_update')

def photo_create(request, self):
	return HttpResponse('photo_create')

