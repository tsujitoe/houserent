from django import forms
from .models import HomeInfo, HomeMediaInfo, HomePhoto

from crispy_forms.helper import FormHelper


class HomeInfoForm(forms.ModelForm):
	class Meta:
		model = HomeInfo
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False        # 我們要自己包。



class HomePhotoForm(forms.ModelForm):
	#h_image = forms.ImageField(required=False)
	class Meta:
		model = HomePhoto
		fields = '__all__'
		