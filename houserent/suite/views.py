from django.shortcuts import redirect, render
from django.http import Http404
# from django.forms.models import modelform_factory
from django.forms.models import inlineformset_factory

from .models import Suites, Rooms
from .forms import SuiteForm, RoomFormSet, SuitePhotoForm

# Create your views here.
def suite_list(request):
    suites = Suites.objects.all()
    return render(request, 'suite_list.html', {'suites': suites})


def suite_detail(request, pk):
    try:
        suite = Suites.objects.get(pk=pk)
    except Suites.DoesNotExist:
        raise Http404
    return render(request, 'suite_detail.html', {'suite': suite})


def suite_create(request):
	if request.method == 'POST':
		form = SuiteForm(request.POST, submit_title='建立')
		if form.is_valid():
			suite=form.save()
			return redirect(suite.get_absolute_url())
	else:
		form = SuiteForm(submit_title='建立')
	return render(request, 'suite_create.html', {'form': form})


def suite_update(request, pk):
	try:
		suite = Suites.objects.get(pk=pk)
	except Suites.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = SuiteForm(request.POST, instance=suite, submit_title='更新')
		if form.is_valid():
			suite = form.save()
			return redirect(suite.get_absolute_url())
	else:
		# 移除 submit button 與 form tag。
		form = SuiteForm(instance=suite, submit_title='更新')
	return render(request, 'suite_update.html', {
		'form': form, 'suite': suite, })



def rooms_update(request, pk):
	try:
		suite = Suites.objects.get(pk=pk)
	except Suites.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		room_formset = RoomFormSet(request.POST, instance=suite)
		if room_formset.is_valid():
			room_formset.save()
			return redirect(suite.get_absolute_url())
	else:
		room_formset = RoomFormSet( instance=suite)
	return render(request, 'rooms_update.html', {
		'room_formset': room_formset, 'suite': suite, })


def model_form_upload(request):
	if request.method == 'POST':
		form = SuitePhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = SuitePhotoForm()
	return render(request, 'model_form_upload.html', {'form': form})



def photo_update(request, pk):
	try:
		suite = Suites.objects.get(pk=pk)
	except Suites.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		photo_form = SuitePhotoForm(request.POST, request.FILES, instance=suite)
		if photo_form.is_valid():
			photo_form.save()
			return redirect(suite.get_absolute_url())
	else:
		photo_form = SuitePhotoForm(instance=suite)
	return render(request, 'photo_update.html', {
		'photo_form': photo_form, 'suite': suite, })

