from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div, InlineField


from django import forms
from django.forms.models import inlineformset_factory
#from django.forms.models import modelformset_factory
#from django.forms.widgets import CheckboxSelectMultiple

from .models import MediaInfo, Media, FakeInfo

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin


class AdminImageWidget(AdminFileWidget):
	def render(self, name, value, attrs=None):
		output = []
		if value and getattr(value, "url", None):
			t = get_thumbnail(value,'300x300')
			output.append('<img src="{}">'.format(t.url))
		output.append(super(AdminFileWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))

class MediaInfoForm(forms.ModelForm):
	#title = forms.CharField(max_length=100)
	class Meta:
		model = MediaInfo
		fields = ('now_type', 'now_address', 'now_phone', 'now_note',)
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		#self.helper.form_tag = False        # 我們要自己包
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))

class MediaForm(forms.ModelForm, AdminImageMixin):
	#image = forms.ImageField()  
	#image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	#image = forms.ModelMultipleChoiceField(queryset=MediaInfo.objects.all())
	class Meta:
		model = Media
		fields = '__all__'
		widgets = {'image': AdminImageWidget,}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False        # 我們要自己包。
		#if submit_title:
		#	self.helper.add_input(Submit('submit', submit_title))
  

BaseMediaInlineFormset = inlineformset_factory(
	parent_model=MediaInfo, model=Media, 
	fields=('image',), extra=1)


class MediaInlineFormset(BaseMediaInlineFormset, AdminImageMixin, ):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		#self.helper.disable_csrf = True
		#self.helper.layout = Layout(InlineField('image','image_note'),)
		#if submit_title:
		#	self.helper.add_input(Submit('submit', submit_title))





# for fake tenant--------------------------

class UrlForm(forms.ModelForm):
	class Meta:
		model = FakeInfo
		fields = ('fake_url',)
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		#self.helper.form_tag = False	# 我們要自己包。
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))

