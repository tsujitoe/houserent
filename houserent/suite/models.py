from django.db import models
from django.core.urlresolvers import reverse #Django1.8.8
# from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
# Create your models here.


class Suite(models.Model):
	inter_item=(
		('公司Key','公司Key'),
		('屋主開門','屋主開門'),
		('管理室','管理室'),
		('密碼','密碼'),
		('請看補充資訊','請看補充資訊'),
	)
	inter_door_item=(
		('公司Key','公司Key'),
		('屋主開門','屋主開門'),
		('管理室','管理室'),
		('藏在現場','藏在現場'),
		('沒鎖','沒鎖'),
		('密碼','密碼'),
		('請看補充資訊','請看補充資訊'),
	)
	type_item=(
		('大樓', '大樓'),
		('公寓', '公寓'),
		('透天', '透天'),
		('其他', '其他'),
	)
	garbage_item=(
		('社區集中','社區集中'),
		('子母車','子母車'),
		('自理','自理'),
		('請看補充資訊','請看補充資訊'),
	)
	wash_item=(
		('獨立','獨立'),
		('公用','公用'),
		('無','無'),
		('請看補充資訊','請看補充資訊'),
	)
	drink_item=(
		('公共','公共'),
		('無','無'),
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
	suite_address=models.CharField(verbose_name='案件地址',default='', blank=True, null=True ,max_length=60)
	suite_master=models.CharField(verbose_name='房東姓名',default='', blank=True, null=True ,max_length=20)
	suite_master_phone=models.CharField(verbose_name='房東電話',default='', blank=True, null=True ,max_length=20)
	suite_how_inter_housedoor=models.CharField(verbose_name='大門如何進入', choices=inter_item, max_length=50)
	suite_how_inter_roomdoor=models.CharField(verbose_name='房門如何進入', choices=inter_door_item, max_length=50)
	#空房狀況
	suite_room=models.TextField(verbose_name='目前空房', default=' ', blank=True, null=True)
	#案件狀況
	suite_type=models.CharField(verbose_name='型態', choices=type_item, blank=True, null=True, max_length=20)
	suite_garbage=models.CharField(verbose_name='垃圾處理', choices=garbage_item, blank=True, null=True, max_length=20)
	suite_wash=models.CharField(verbose_name='洗衣', choices=wash_item, blank=True, null=True, max_length=20)
	suite_drink=models.CharField(verbose_name='飲水', choices=drink_item, blank=True, null=True, max_length=20)
	#租金包含
	suite_elecfee=models.CharField(verbose_name='電費計算', default='5元 | 台電,',max_length=10)
	suite_include=MultiSelectField(verbose_name='包含雜費',choices=include_items, blank=True, null=True, max_length=100)
	suite_fee_note=models.TextField(verbose_name='雜費補充', default=' | 管理費： \n | 電費： \n | 水費： \n | 其他： ')
	#限制條件
	suite_pet_limit=MultiSelectField(verbose_name='寵物限制', choices=pet_item, blank=True, null=True, max_length=100)
	suite_people_limit=MultiSelectField(verbose_name='身份限制', choices=people_item, blank=True, null=True, max_length=100)
	#補充資訊
	suite_note=models.TextField(verbose_name='補充資訊', default=' | 如何進入大門： \n | 管理方式： \n | 垃圾處理： \n | 其他限制問題： \n')
	class Meta:
		verbose_name_plural='套房案件'
	def __str__(self):
		return self.suite_address
	def get_absolute_url(self):
		return reverse('suite_detail', kwargs={'pk': self.pk})

"""
class Room(models.Model):
	room_address=models.ForeignKey(Suite, on_delete=models.SET_NULL, blank=True, null=True, related_name='rooms')
	room_fullrent=models.BooleanField(verbose_name='可租', default=True)
	room_number=models.CharField(verbose_name='房號', max_length=10, default='.')
	room_rent=models.PositiveIntegerField(verbose_name='價位', blank=True, null=True)
	room_description=models.TextField(verbose_name='備註', default=' ', blank=True, null=True, max_length=50)
	class Meta:
		verbose_name_plural='空房資訊'
	def __str__(self):
		return self.room_number
"""



class SuitePhotoInfo(models.Model):
	s_address=models.ForeignKey(Suite, on_delete=models.SET_NULL, blank=True, null=True, related_name='title_photo')
	s_title=models.CharField(verbose_name='標題', default='', max_length=60)
	class Meta:
		verbose_name_plural='照片資訊'
	def __str__(self):
		return self.home_title

class SuitePhoto(models.Model):
	s_title=models.ForeignKey(SuitePhotoInfo, verbose_name='標題', on_delete=models.SET_NULL, blank=True, null=True, related_name='photo')
	s_image = models.FileField(verbose_name='照片', default='', upload_to='suite_photo/%Y-%m-%d', )
	s_date = models.DateTimeField(auto_now_add=True,)
	class Meta:
		verbose_name_plural='套房照片'
	def image_tag(self):
		if self.h_image :
			return u'<img src="%s" width="300px" />' % self.h_image.url
	image_tag.short_description = '圖片'
	image_tag.allow_tags = True
