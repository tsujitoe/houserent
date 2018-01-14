from .models import JPicture

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
#from crispy_forms.bootstrap import InlineCheckboxes

from django import forms
#from django.forms.widgets import CheckboxSelectMultiple
#from django.forms.models import inlineformset_factory


class StreetForm(forms.ModelForm):
	class Meta:
		model = Picture
		#fields = ('street',)
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		#self.helper.form_tag = False	# 我們要自己包。
		self.helper.layout = Layout(
			HTML("""

				"""),
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))
