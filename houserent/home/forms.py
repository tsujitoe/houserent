from django import forms
from .models import HomeInfo, HomeMediaInfo, HomePhoto

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div

class HomeInfoForm(forms.ModelForm):
	class Meta:
		model = HomeInfo
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False  # 我們要自己包。
		self.helper.layout = Layout(
			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">基本資訊</h2></div><div class="panel-body">'),
			Div(
				Div('home_address', css_class="col-sm-8", ),
				Div('home_how_inter_door', css_class="col-sm-4"),
				css_class = 'row'
				), 
			Div(
				Div('home_master', css_class="col-sm-6"),
				Div('home_master_phone', css_class="col-sm-6"),
				css_class = 'row'
				), 
			
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">租金細目</h2></div><div class="panel-body">'),
			'home_rent',
			InlineCheckboxes('home_include'),
			Field('home_fee_note' ,rows=5, ),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">案件格局</h2></div><div class="panel-body">'),
			Div(
				Div('home_square', css_class="col-sm-3"),
				Div('home_type', css_class="col-sm-3"),
				Div('home_how_manage', css_class="col-sm-3"),
				Div('home_garbage', css_class="col-sm-3"),
				css_class = 'row'
				), 
			'home_park',
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">設備</h2></div><div class="panel-body">'),
			InlineCheckboxes('home_equipment'),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">條件限制與其他資訊補充</h2></div><div class="panel-body">'),
			InlineCheckboxes('home_pet_limit'),
			InlineCheckboxes('home_people_limit'),
			Field('home_note' ,rows=5, ),
			HTML('</div></div>'),
		)


"""

<div class="panel panel-info">
	<div class="panel-heading">
		<h2 class="panel-title">新增 住家案件</h2>
	</div>
    <div class="panel-body">
		<form method="post" enctype="multipart/form-data">
			{% csrf_token %}
			{% crispy home_form %}
	</div>



<label class="checkbox-inline">
</label>
"""

class HomePhotoForm(forms.ModelForm):
	#h_image = forms.ImageField(required=False)
	class Meta:
		model = HomePhoto
		fields = '__all__'
		