from django import forms
from .models import StoreInfo, StoreMediaInfo, StorePhoto

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from crispy_forms.bootstrap import InlineCheckboxes, Field, Div

class StoreInfoForm(forms.ModelForm):
	class Meta:
		model = StoreInfo
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False  # 我們要自己包。
		#self.helper.form_show_labels = False
		self.helper.layout = Layout(
			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">基本資訊</h2></div><div class="panel-body">'),
			Div(
				Div(Field('store_address' ,placeholder="詳細地址：台中市西區中美街416號2樓"), css_class="col-sm-8", ),
				Div('store_how_inter_door', css_class="col-sm-4"),
				css_class = 'row'
				), 
			Div(
				Div(Field('store_master',placeholder="隔壁的老王?"), css_class="col-sm-6"),
				Div(Field('store_master_phone',placeholder="格式要正確，範例：0938-389-945"), css_class="col-sm-6"),
				css_class = 'row'
				), 
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">租金細目</h2></div><div class="panel-body">'),
			Field('store_rent',placeholder="租金多少錢?"),
			InlineCheckboxes('store_include'),
			Field('store_fee_note' ,rows=5, ),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">案件格局</h2></div><div class="panel-body">'),
			Div(
				Div('store_type', css_class="col-sm-3"),
				Div(Field('store_floor', placeholder="可使樓層"), css_class="col-sm-3"),
				Div(Field('store_partten', placeholder="隔間間數?幾間廁所?"), css_class="col-sm-3"),
				Div(Field('store_square', placeholder="可使用坪數(目測)"), css_class="col-sm-3"),
				css_class = 'row'
				), 
			Div(
				Div('store_how_manage', css_class="col-sm-3"),
				Div('store_garbage', css_class="col-sm-3"),
				Div(Field('store_park', placeholder="範例：車號：B4-203，機上"), css_class="col-sm-6"),
				css_class = 'row'
				),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">設備</h2></div><div class="panel-body">'),
			InlineCheckboxes('store_equipment'),
			HTML('</div></div>'),

			HTML('<div class="panel panel-info"><div class="panel-heading"><h2 class="panel-title">條件限制與其他資訊補充</h2></div><div class="panel-body">'),
			InlineCheckboxes('store_people_limit', css_class=""),
			Field('store_note' ,rows=5, ),
			HTML('</div></div>'),
		)



class StorePhotoForm(forms.ModelForm):
	#h_image = forms.ImageField(required=False)
	class Meta:
		model = StorePhoto
		fields = '__all__'
		