
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.files.base import ContentFile
import os.path

from .models import HomeInfo, HomeMediaInfo, HomePhoto
from .forms import HomeInfoForm, HomePhotoForm


def home_info_list(request):
	home_info = HomeInfo.objects.all()
	return render(request, 'home_list.html', {'home_info': home_info})

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
			home_info.home_partten=home_form.cleaned_data['home_partten'] 
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

			return redirect(home_info.get_absolute_url())
		else:
			print(home_form.errors)
			return HttpResponse('upload QQ !')
	else:
		home_form = HomeInfoForm()
	return render(request,'upload_home_info.html', {'home_form': home_form})



def home_info_detail(request, pk):
	try:
		home_info = HomeInfo.objects.get(pk=pk)
	except HomeInfo.DoesNotExist:
		raise Http404
	return render(request, 'home_detail.html', {'home_info': home_info})


def home_info_update(request, pk):	
	try:
		home_info = HomeInfo.objects.get(pk=pk)
	except HomeInfo.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = HomeInfoForm(request.POST, instance=home_info)
		if form.is_valid():
			home_info=form.save()
			return redirect(home_info.get_absolute_url())
	else:
		form = HomeInfoForm(instance=home_info)
	return render(request, 'home_update.html', {'form': form, 'home_info': home_info, })


def photo_create(request, pk):
	try:
		# 1 agree
		home_info = HomeInfo.objects.get(pk=pk)
	except HomeInfo.DoesNotExist:
		raise Http404
	if request.method == "POST":
		# 2 agree
		info_title = request.POST.get('title', '')
		info = HomeMediaInfo.objects.create(home_address=home_info, home_title=info_title)
		info.save()
		# 3 agree
		if 'docfile' in request.FILES:
			image_list = request.FILES.getlist('docfile')
			for a_image in image_list:
				s = HomePhoto.objects.create(h_title=info, h_image=a_image)
				s.save()
		else:
			return HttpResponse('照片存失敗了')
		return redirect(home_info.get_absolute_url())
	return render(request, 'upload_image.html', {'home_info':home_info})



