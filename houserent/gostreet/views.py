from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.forms.models import inlineformset_factory

from .models import MediaInfo, Media
from .forms import MediaInfoForm, MediaForm, MediaInlineFormset
#from .models import Post, Images_street
#from .forms import PostForm, ImageForm, ImageFormSet

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


def  street_detail(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk)
	except MediaInfo.DoesNotExist:
		raise Http404
	return render(request, 'street_detail.html', {'address': address})


def street_image(request, pk):
	try:
		address = MediaInfo.objects.get(pk=pk)
	except MediaInfo.DoesNotExist:
		raise Http404
	if request.method == "POST":
		#form = MediaInfoForm(request.POST, instance=address, submit_title='建立')
		formset = MediaInlineFormset(request.POST, instance=address, submit_title='上傳')
		#formset = MediaInlineFormset(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			return redirect(address.get_absolute_url())
	else:
		#form = MediaInfo(instance=address, submit_title=None)
		formset = MediaInlineFormset(instance=address)
	return render(request, 'street_image.html', {'address':address, 'formset':formset})




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
