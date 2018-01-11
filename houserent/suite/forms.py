from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import inlineformset_factory


from .models import Suites, Rooms, SuitePhoto

class SuiteForm(forms.ModelForm):
	suite_include = forms.MultipleChoiceField(choices=Suites.include_items, widget=forms.CheckboxSelectMultiple())
	class Meta:
		model = Suites
		fields = ('suite_address',
			'suite_how_inter_housedoor', 'suite_how_inter_roomdoor', 
			'suite_include', 'suite_no_include', 'suite_elecfee', 
			'suite_garbage', 'suite_wash', 'suite_drink', 
			'suite_limit', 'suite_note')
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['suite_include'].label = '租金包含'

		self.helper.layout = Layout(
			Fieldset('案件進入:',
				Field('suite_address', 'suite_how_inter_housedoor', 'suite_how_inter_roomdoor', css_class='input-sm',),
				style="color: brown;",
				),

			Fieldset('租金細節:',
				Field('suite_elecfee', css_class='input-sm',),
				InlineCheckboxes('suite_include'),
				Field('suite_no_include', css_class='input-sm',),
				style="color: brown;",
					),
			Fieldset('設備包含:',
				Field('suite_garbage', 'suite_wash', 'suite_drink', css_class='input-sm',),
				style="color: brown;",
				),
			Fieldset('其他條件:',
				Field('suite_limit', css_class='input-sm',), 
				Field('suite_note' ,rows=3, css_class='input-xlarge'),
				style="color: brown;",
				),
			)
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))

BaseRoomFormSet = inlineformset_factory(
	parent_model=Suites, model=Rooms, 
	fields=('room_fullrent', 'room_number', 'room_rent', 
		'room_description'), 
	extra=1,)

class RoomFormSet(BaseRoomFormSet):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False        # 我們要自己包。

"""
BasePhotoFormSet = inlineformset_factory(
	parent_model=Suites, model=Suite_photo, 
	fields=('p_subject', 'p_image', ), 
	extra=1,)
"""


class SuitePhotoForm(forms.ModelForm):
	p_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = SuitePhoto
		fields = ('p_subject', 'p_image', )
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False        # 我們要自己包。


"""
class SuitePhotoForm(forms.ModelForm):
	#p_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = Suite_photo
		fields=('p_subject', 'p_image', )
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))
"""
