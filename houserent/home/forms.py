from django import forms
from .models import HomeMediaInfo, HomePhoto


class HomePhotoForm(forms.ModelForm):
	#h_image = forms.ImageField(required=False)
	class Meta:
		model = HomePhoto
		fields = '__all__'
		