from django.db import models
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
# my_field2 = MultiSelectField(choices=MY_CHOICES2, max_choices=3, max_length=3)

# Create your models here.

class StoreInfo(models.Model):
	inter_item=(
		('公司Key','公司Key'),
		('屋主開門','屋主開門'),
		('管理室','管理室'),
		('密碼','密碼'),
		('請看補充資訊','請看補充資訊'),
	)
	type_item=(
		('透店', '透店'),
		('樓店', '樓店'),
		('小商場', '小商場'),
		('大商場', '大商場'),
		('辦公室', '辦公室'),
		('廠房', '廠房'),
		('土地', '土地'),
		('請看補充資訊','請看補充資訊'),
	)
	manage_item=(
		('無','無'),
		('物管公司','物管公司'),
		('管理員','管理員'),
		('請看補充資訊','請看補充資訊'),
	)
	garbage_item=(
		('自理','自理'),
		('社區集中','社區集中'),
		('子母車','子母車'),
		('請看補充資訊','請看補充資訊'),
	)
	include_items=(
		('稅', '稅'),
		('水', '水'),
		('網路', '網路'),
		('第四台', '第四台'),
		('垃圾費', '垃圾費'),
		('管理費', '管理費'),
		('其他', '其他'),
	)
	equipment_item=(
		('桌子', '桌子'),
		('椅子', '椅子'),
		('衣櫃', '衣櫃'),
		('床組', '床組'),
		('沙發', '沙發'),
		('電視', '電視'),
		('冰箱', '冰箱'),
		('冷氣', '冷氣'),
		('熱水器', '熱水器'),
		('洗衣機', '洗衣機'),
	)
	people_item=(
		('要公證','要公證'),
		('禁報稅','禁報稅'),
		('禁八大','禁八大'),
		('全禁餐飲','全禁餐飲'),
		('可飲料店','可飲料店'),
		('可輕食店','可輕食店'),
		('請看補充資訊','請看補充資訊'),
	)

	#基本資料
	store_address=models.CharField(verbose_name='案件地址', default='' ,max_length=100)
	store_master=models.CharField(verbose_name='房東姓名', blank=True, null=True ,max_length=20)
	store_master_phone=models.CharField(verbose_name='房東電話', blank=True, null=True ,max_length=20)
	store_how_inter_door=models.CharField(verbose_name='如何進入房門', choices=inter_item, blank=True, null=True, max_length=50)
	#案件格局
	store_type=models.CharField(verbose_name='型態', choices=type_item, blank=True, null=True, max_length=20)
	store_floor=models.CharField(verbose_name='使用樓層', default='', blank=True, null=True, max_length=20)
	store_square=models.CharField(verbose_name='坪數', default='', blank=True, null=True, max_length=10)
	store_how_manage=models.CharField(verbose_name='管理方式', choices=manage_item , blank=True, null=True, max_length=20)
	store_garbage=models.CharField(verbose_name='垃圾處理', choices=garbage_item, blank=True, null=True, max_length=20)
	store_partten=models.CharField(verbose_name='格局', default='', blank=True, null=True, max_length=50)
	store_park=models.CharField(verbose_name='車位', default='', blank=True, null=True, max_length=50)
	#租金細目
	store_rent=models.CharField(verbose_name='租金', default='', blank=True, null=True, max_length=20)
	store_include=MultiSelectField(verbose_name='包含雜費',choices=include_items, blank=True, null=True, max_length=100)
	store_fee_note=models.TextField(verbose_name='雜費補充', default='租金含稅： \n管理費： \n電費： \n水費： \n其他： ')
	#設備包含
	store_equipment=MultiSelectField(verbose_name='設備包含',choices=equipment_item, blank=True, null=True, max_length=100)
	#條件限制
	store_people_limit=MultiSelectField(verbose_name='租客限制', choices=people_item, blank=True, null=True, max_length=100)
	#補充資訊
	store_note=models.TextField(verbose_name='補充資訊', default='如何進入大門： \n管理方式： \n垃圾處理： \n其他限制問題： \n')
	class Meta:
		verbose_name_plural='店面案件'
	def __str__(self):
		return self.store_address
	def get_absolute_url(self):
		return reverse('store_info_detail', kwargs={'pk': self.pk})
	


class StoreMediaInfo(models.Model):
	store_address=models.ForeignKey(StoreInfo, on_delete=models.SET_NULL, blank=True, null=True, related_name='title_photo')
	store_title=models.CharField(verbose_name='標題', default='', max_length=60)
	class Meta:
		verbose_name_plural='照片資訊'
	def __str__(self):
		return self.store_title



class StorePhoto(models.Model):
	s_title=models.ForeignKey(StoreMediaInfo, verbose_name='標題', on_delete=models.SET_NULL, blank=True, null=True, related_name='photo')
	s_image = models.FileField(verbose_name='照片', default='', upload_to='store_photo/%Y-%m-%d', )
	s_date = models.DateTimeField(auto_now_add=True,)
	class Meta:
		verbose_name_plural='店面照片'
	def image_tag(self):
		if self.s_image :
			return u'<img src="%s" width="300px" />' % self.s_image.url
	image_tag.short_description = '圖片'
	image_tag.allow_tags = True

