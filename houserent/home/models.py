from django.db import models
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
# my_field2 = MultiSelectField(choices=MY_CHOICES2, max_choices=3, max_length=3)

# Create your models here.

class HomeInfo(models.Model):
	inter_item=(
		('公司Key','公司Key'),
		('屋主開門','屋主開門'),
		('管理室','管理室'),
		('密碼','密碼'),
		('其他補充','其他補充'),
	)
	type_item=(
		('大樓', '大樓'),
		('公寓', '公寓'),
		('透天', '透天'),
		('其他', '其他'),
	)
	manage_item=(
		('物管公司','物管公司'),
		('管理員','管理員'),
		('無','無'),
		('其他補充','其他補充'),
	)
	garbage_item=(
		('社區集中','社區集中'),
		('子母車','子母車'),
		('自理','自理'),
		('其他補充','其他補充'),
	)
	include_items=(
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
		('床', '床'),
		('沙發', '沙發'),
		('熱水器', '熱水器'),
		('電視', '電視'),
		('冰箱', '冰箱'),
		('冷氣', '冷氣'),
		('洗衣機', '洗衣機'),
	)
	pet_item=(
		('全部禁寵','全部禁寵'),
		('可寵','可寵'),
		('可貓','可貓'),
		('可狗','可狗'),
		('其他補充','其他補充'),
	)
	people_item=(
		('學生','學生'),
		('上班族','上班族'),
		('家庭','家庭'),
		('禁男','禁男'),
		('禁女','禁女'),
		('禁小孩','禁小孩'),
		('禁40以上','禁40以上'),
		('禁拜拜','禁拜拜'),
		('禁煮飯','禁煮飯'),
		('其他補充','其他補充'),
	)

	#基本資料
	home_address=models.CharField(verbose_name='案件地址', blank=True, null=True ,max_length=60)
	home_master=models.CharField(verbose_name='房東姓名', blank=True, null=True ,max_length=20)
	home_master_phone=models.CharField(verbose_name='房東電話', blank=True, null=True ,max_length=20)
	home_how_inter_door=models.CharField(verbose_name='如何進入房門', choices=inter_item, blank=True, null=True, max_length=50)
	#案件格局
	home_type=models.CharField(verbose_name='型態', choices=type_item, blank=True, null=True, max_length=20)
	home_square=models.CharField(verbose_name='坪數', default='10', max_length=10)
	home_how_manage=models.CharField(verbose_name='管理方式', choices=manage_item , blank=True, null=True, max_length=20)
	home_garbage=models.CharField(verbose_name='垃圾處理', choices=garbage_item, blank=True, null=True, max_length=20)
	home_park=models.CharField(verbose_name='車位', default='平面 | 機上/下，車號：', max_length=50)
	#租金細目
	home_rent=models.CharField(verbose_name='租金', blank=True, null=True, default='5000', max_length=20)
	home_include=MultiSelectField(verbose_name='包含雜費',choices=include_items, blank=True, null=True, max_length=100)
	home_fee_note=models.TextField(verbose_name='雜費補充', default='管理費： \n電費： \n水費： \n其他： ')
	#設備包含
	home_equipment=MultiSelectField(verbose_name='設備包含',choices=equipment_item, blank=True, null=True, max_length=100)
	#條件限制
	home_pet_limit=MultiSelectField(verbose_name='寵物限制', choices=pet_item, blank=True, null=True, max_length=100)
	home_people_limit=MultiSelectField(verbose_name='身份限制', choices=people_item, blank=True, null=True, max_length=100)
	#補充資訊
	home_note=models.TextField(verbose_name='補充資訊', default='有無密碼： \n管理方式： \n垃圾處理： \n其他限制： \n')
	class Meta:
		verbose_name_plural='住宅案件'
	def __str__(self):
		return self.home_address
	def get_absolute_url(self):
		return reverse('home_info_detail', kwargs={'pk': self.pk})




class HomeMediaInfo(models.Model):
	home_address=models.ForeignKey(HomeInfo, on_delete=models.SET_NULL, blank=True, null=True, related_name='title_photo')
	home_title=models.CharField(verbose_name='標題', blank=True, null=True ,max_length=60)
	class Meta:
		verbose_name_plural='照片資訊'
	def __str__(self):
		return self.home_title
	#def get_absolute_url(self):
	#	return reverse('home_media_info', kwargs={'pk': self.pk})

class HomePhoto(models.Model):
	h_title=models.ForeignKey(HomeMediaInfo, verbose_name='標題', on_delete=models.SET_NULL, blank=True, null=True, related_name='photo')
	h_image = models.FileField(verbose_name='照片', upload_to='home_photo/%Y-%m-%d', null=True, blank=True)
	h_date = models.DateTimeField(auto_now_add=True,)
	class Meta:
		verbose_name_plural='住宅照片'
	def image_tag(self):
		if self.h_image :
			return u'<img src="%s" width="300px" />' % self.h_image.url
	image_tag.short_description = '圖片'
	image_tag.allow_tags = True

