
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.files.base import ContentFile
import os.path

from .models import HomeInfo, HomeMediaInfo, HomePhoto
from .forms import HomeInfoForm, HomePhotoForm


def post_upload_images_test_database(request):
	if request.method == 'POST':
		home_form = HomeInfoForm(request.POST, request.FILES)
		#img_form = HomePhotoForm(request.POST, request.FILES)
		#if home_form.is_valid() and img_form.is_valid():
		if home_form.is_valid() :
			# 1 agree
			home_info = HomeInfo.objects.create()
			home_info.home_address=home_form.cleaned_data['home_address'] 
			home_info.home_master=home_form.cleaned_data['home_master'] 
			home_info.home_master_phone=home_form.cleaned_data['home_master_phone'] 
			home_info.home_how_manage=home_form.cleaned_data['home_how_manage'] 
			home_info.home_how_inter_door=home_form.cleaned_data['home_how_inter_door'] 

			home_info.home_no_include=home_form.cleaned_data['home_no_include'] 
			home_info.home_elecfee=home_form.cleaned_data['home_elecfee'] 
			home_info.home_garbage=home_form.cleaned_data['home_garbage'] 
			home_info.home_wash=home_form.cleaned_data['home_wash'] 
			home_info.home_drink=home_form.cleaned_data['home_drink'] 
			home_info.home_pet=home_form.cleaned_data['home_pet'] 
			home_info.home_limit=home_form.cleaned_data['home_limit'] 
			home_info.home_note=home_form.cleaned_data['home_note'] 
			home_info.save()

			"""
			home_address = request.POST.get('address', '')
			home_info = HomeInfo.objects.create(home_address = home_address)
			home_info.save()
			"""


			# 2 agree
			info_title = request.POST.get('title', '')
			info = HomeMediaInfo.objects.create(home_address=home_info, home_title = info_title)
			info.save()

			# 3 agree
			if 'docfile' in request.FILES:
				image_list = request.FILES.getlist('docfile')
				for a_image in image_list:
					s = HomePhoto(h_title=info, h_image=a_image)
					s.save()
				return HttpResponse('upload ok!')
			else:
				return redirect('/upload/')
		else:
			image = None
			return HttpResponse('upload QQ !')
	else:
		home_form = HomeInfoForm()
	return render(request,'upload_image.html', {'home_form': home_form})
