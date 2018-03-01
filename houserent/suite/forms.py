from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset,  HTML
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import inlineformset_factory


from .models import Suite, SuitePhoto

class SuiteForm(forms.ModelForm):
	#suite_include = forms.MultipleChoiceField(choices=Suite.include_items, widget=forms.CheckboxSelectMultiple())
	class Meta:
		model = Suite
		fields = ('__all__')
	def __init__(self, *args, submit_title='Submit', **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		#self.fields['suite_include'].label = '租金包含'
		self.helper.layout = Layout(
			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">基本資訊</h2></div><div class="panel-body">'),
			Div(
				Div(Field('suite_address' ,placeholder="詳細地址：台中市西區中美街416號2樓"), css_class="col-sm-6", ),
				Div('suite_how_inter_housedoor', css_class="col-sm-3"),
				Div('suite_how_inter_roomdoor', css_class="col-sm-3"),
				css_class = 'row'
				), 
			Div(
				Div(Field('suite_master',placeholder="隔壁的老王?"), css_class="col-sm-6"),
				Div(Field('suite_master_phone',placeholder="格式要正確，範例：0938-389-945"), css_class="col-sm-6"),
				css_class = 'row'
				), 
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">案件狀況</h2></div><div class="panel-body">'),
			Div(
				Div('suite_type', css_class="col-sm-3"),			
				Div('suite_garbage', css_class="col-sm-3"),
				Div('suite_wash', css_class="col-sm-3"),
				Div('suite_drink', css_class="col-sm-3"),
				css_class = 'row'
				), 
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">租金包含</h2></div><div class="panel-body">'),
			'suite_elecfee',
			InlineCheckboxes('suite_include'),
			Field('suite_fee_note' ,rows=5, ),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">條件限制與其他資訊補充</h2></div><div class="panel-body">'),
			InlineCheckboxes('suite_pet_limit'),
			InlineCheckboxes('suite_people_limit', css_class=""),
			Field('suite_note' ,rows=5, ),
			HTML('</div></div>'),
		)
		if submit_title:
			self.helper.add_input(Submit('submit', submit_title))


class RoomForm(forms.ModelForm):
	class Meta:
		model = Suite
		fields = ('suite_room', )
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False # 我們要自己包
		self.helper.form_show_labels = False
		
"""
BaseRoomFormSet = inlineformset_factory(
	parent_model=Suite, model=Room, form=RoomForm, extra=1,)
class RoomFormSet(BaseRoomFormSet):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.disable_csrf = True
		#self.helper.form_show_labels = False
		self.helper.layout = Layout(
			Div(
				Div(Field('DELETE',placeholder=""), css_class="col-sm-1"),
				Div(Field('room_fullrent',), css_class="col-sm-1"),
				Div(Field('room_number',placeholder=""), css_class="col-sm-2"),
				Div(Field('room_rent',placeholder=""), css_class="col-sm-2"),
				Div(Field('room_description',placeholder=""), css_class="col-sm-6"),
				css_class = 'row'
			), 

		)
"""



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
		fields = ('s_title', 's_image', )
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
