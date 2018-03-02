from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from .models import StoreInfo, StoreMediaInfo, StorePhoto
from .forms import StoreInfoForm, StorePhotoForm
# Create your views here.

def store_info_list(request):
	store_info = StoreInfo.objects.all()
	return render(request, 'store_list.html', {'store_info': store_info})

def store_info_create(request):
	if request.method == 'POST':
		store_form = StoreInfoForm(request.POST, request.FILES)
		if store_form.is_valid():
			store_info=store_form.save()
			return redirect(store_info.get_absolute_url())
		else:
			print(store_form.errors)
			return HttpResponse('upload QQ !')
	else:
		store_form = StoreInfoForm()
	return render(request,'upload_store_info.html', {'store_form': store_form})

def store_info_detail(request, pk):
	try:
		store_info = StoreInfo.objects.get(pk=pk)
	except StoreInfo.DoesNotExist:
		raise Http404
	return render(request, 'store_detail.html', {'store_info': store_info})

def store_info_update(request, pk):	
	try:
		store_info = StoreInfo.objects.get(pk=pk)
	except StoreInfo.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = StoreInfoForm(request.POST, instance=store_info)
		if form.is_valid():
			store_info=form.save()
			return redirect(store_info.get_absolute_url())
	else:
		form = StoreInfoForm(instance=store_info)
	return render(request, 'store_update.html', {'form': form, 'store_info': store_info, })

def photo_create(request, pk):
	try:
		# 1 agree
		store_info = StoreInfo.objects.get(pk=pk)
	except StoreInfo.DoesNotExist:
		raise Http404
	if request.method == "POST":
		# 2 agree
		info_title = request.POST.get('title', '')
		info = StoreMediaInfo.objects.create(store_address=store_info, store_title=info_title)
		info.save()
		# 3 agree
		if 'docfile' in request.FILES:
			image_list = request.FILES.getlist('docfile')
			for a_image in image_list:
				s = StorePhoto.objects.create(s_title=info, s_image=a_image)
				s.save()
		else:
			return HttpResponse('照片存失敗了')
		return redirect(store_info.get_absolute_url())
	return render(request, 'upload_image.html', {'store_info':store_info})



