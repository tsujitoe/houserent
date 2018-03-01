from django import forms
from .models import HomeInfo, HomeMediaInfo, HomePhoto

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div

class HomeInfoForm(forms.ModelForm):
	class Meta:
		model = HomeInfo
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False  # 我們要自己包。
		#self.helper.form_show_labels = False
		self.helper.layout = Layout(
			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">基本資訊</h2></div><div class="panel-body">'),
			Div(
				Div(Field('home_address' ,placeholder="詳細地址：台中市西區中美街416號2樓"), css_class="col-sm-8", ),
				Div('home_how_inter_door', css_class="col-sm-4"),
				css_class = 'row'
				), 
			Div(
				Div(Field('home_master',placeholder="隔壁的老王?"), css_class="col-sm-6"),
				Div(Field('home_master_phone',placeholder="格式要正確，範例：0938-389-945"), css_class="col-sm-6"),
				css_class = 'row'
				), 
			
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">租金細目</h2></div><div class="panel-body">'),
			Field('home_rent',placeholder="租金多少錢?"),
			InlineCheckboxes('home_include'),
			Field('home_fee_note' ,rows=5, ),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">案件格局</h2></div><div class="panel-body">'),
			Div(
				Div(Field('home_square', placeholder="目測大概坪數"), css_class="col-sm-3"),
				Div('home_type', css_class="col-sm-3"),
				Div('home_how_manage', css_class="col-sm-3"),
				Div('home_garbage', css_class="col-sm-3"),
				css_class = 'row'
				), 
			Div(
				Div(Field('home_partten', placeholder="3房2廳1衛1陽，簡寫3R2T1W1Y"), css_class="col-sm-6"),
				Div(Field('home_park', placeholder="範例：車號：B4-203，機上"), css_class="col-sm-6"),
				css_class = 'row'
				),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">設備</h2></div><div class="panel-body">'),
			InlineCheckboxes('home_equipment'),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">條件限制與其他資訊補充</h2></div><div class="panel-body">'),
			InlineCheckboxes('home_pet_limit'),
			InlineCheckboxes('home_people_limit', css_class=""),
			Field('home_note' ,rows=5, ),
			HTML('</div></div>'),
		)


class HomePhotoForm(forms.ModelForm):
	#h_image = forms.ImageField(required=False)
	class Meta:
		model = HomePhoto
		fields = '__all__'
		