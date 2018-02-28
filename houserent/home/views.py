
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.files.base import ContentFile
import os.path

from .models import HomeInfo, HomeMediaInfo, HomePhoto
from .forms import HomePhotoForm


def post_upload_images_test_database(request):
	
	if request.method == 'POST':
		
		img_form = HomePhotoForm(request.POST, request.FILES)
		if img_form.is_valid():

			# 1 agree
			home_address = request.POST.get('address', '')
			home_info = HomeInfo.objects.create(home_address = home_address)
			home_info.save()

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
		return render(request,'upload_image.html')
