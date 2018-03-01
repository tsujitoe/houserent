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
		('請看補充資訊','請看補充資訊'),
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
		('請看補充資訊','請看補充資訊'),
	)
	garbage_item=(
		('社區集中','社區集中'),
		('子母車','子母車'),
		('自理','自理'),
		('請看補充資訊','請看補充資訊'),
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
		('床組', '床組'),
		('沙發', '沙發'),
		('電視', '電視'),
		('冰箱', '冰箱'),
		('冷氣', '冷氣'),
		('熱水器', '熱水器'),
		('洗衣機', '洗衣機'),
	)
	pet_item=(
		('可寵','可寵'),
		('可貓','可貓'),
		('可狗','可狗'),
		('全部禁寵','全部禁寵'),
		('請看補充資訊','請看補充資訊'),
	)
	people_item=(
		('學生','學生'),
		('家庭','家庭'),
		('上班族','上班族'),
		('禁男','禁男'),
		('禁女','禁女'),
		('禁小孩','禁小孩'),
		('禁拜拜','禁拜拜'),
		('禁煮飯','禁煮飯'),
		('請看補充資訊','請看補充資訊'),
	)

	#基本資料
	home_address=models.CharField(verbose_name='案件地址', default='' ,max_length=100)
	home_master=models.CharField(verbose_name='房東姓名', blank=True, null=True ,max_length=20)
	home_master_phone=models.CharField(verbose_name='房東電話', blank=True, null=True ,max_length=20)
	home_how_inter_door=models.CharField(verbose_name='如何進入房門', choices=inter_item, blank=True, null=True, max_length=50)
	#案件格局
	home_type=models.CharField(verbose_name='型態', choices=type_item, blank=True, null=True, max_length=20)
	home_square=models.CharField(verbose_name='坪數', default='', blank=True, null=True, max_length=10)
	home_how_manage=models.CharField(verbose_name='管理方式', choices=manage_item , blank=True, null=True, max_length=20)
	home_garbage=models.CharField(verbose_name='垃圾處理', choices=garbage_item, blank=True, null=True, max_length=20)
	home_partten=models.CharField(verbose_name='格局', default='', blank=True, null=True, max_length=50)
	home_park=models.CharField(verbose_name='車位', default='', blank=True, null=True, max_length=50)
	#租金細目
	home_rent=models.CharField(verbose_name='租金', default='', blank=True, null=True, max_length=20)
	home_include=MultiSelectField(verbose_name='包含雜費',choices=include_items, blank=True, null=True, max_length=100)
	home_fee_note=models.TextField(verbose_name='雜費補充', default='管理費： \n電費： \n水費： \n其他： ')
	#設備包含
	home_equipment=MultiSelectField(verbose_name='設備包含',choices=equipment_item, blank=True, null=True, max_length=100)
	#條件限制
	home_pet_limit=MultiSelectField(verbose_name='寵物限制', choices=pet_item, blank=True, null=True, max_length=100)
	home_people_limit=MultiSelectField(verbose_name='身份限制', choices=people_item, blank=True, null=True, max_length=100)
	#補充資訊
	home_note=models.TextField(verbose_name='補充資訊', default='如何進入大門： \n管理方式： \n垃圾處理： \n其他限制問題： \n')
	class Meta:
		verbose_name_plural='住宅案件'
	def __str__(self):
		return self.home_address
	def get_absolute_url(self):
		return reverse('home_info_detail', kwargs={'pk': self.pk})
	


class HomeMediaInfo(models.Model):
	home_address=models.ForeignKey(HomeInfo, on_delete=models.SET_NULL, blank=True, null=True, related_name='title_photo')
	home_title=models.CharField(verbose_name='標題', default='', max_length=60)
	class Meta:
		verbose_name_plural='照片資訊'
	def __str__(self):
		return self.home_title
	def get_absolute_url_admin_edit(self):
		return '../../../admin/home/homemediainfo/%s/change/' % self.pk
	def url_tag(self):
		#return u'<a href="%s" target="_blank">%s</a>' % self.get_absolute_url_admin_edit, self.home_title
		return 'hello'
	url_tag.short_description = 'Link'
	url_tag.allow_tags = True



class HomePhoto(models.Model):
	h_title=models.ForeignKey(HomeMediaInfo, verbose_name='標題', on_delete=models.SET_NULL, blank=True, null=True, related_name='photo')
	h_image = models.FileField(verbose_name='照片', default='', upload_to='home_photo/%Y-%m-%d', )
	h_date = models.DateTimeField(auto_now_add=True,)
	class Meta:
		verbose_name_plural='住宅照片'
	def image_tag(self):
		if self.h_image :
			return u'<img src="%s" width="300px" />' % self.h_image.url
	image_tag.short_description = '圖片'
	image_tag.allow_tags = True

