from django.db import models
from django.core.urlresolvers import reverse #Django1.8.8
# from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Suites(models.Model):
	include_items=(
		('水', '水'),
		('電', '電'),
		('網路', '網路'),
		('第四台', '第四台'),
		('垃圾費', '垃圾費'),
		('管理費', '管理費'),
		('其他', '其他'),
	)

	suite_address=models.CharField(verbose_name='案件地址', blank=True, null=True ,max_length=60)
	suite_how_inter_housedoor=models.CharField(verbose_name='如何進入案件', default='公司Key | 密碼 | 管理室 | 屋主開門', max_length=50)
	suite_how_inter_roomdoor=models.CharField(verbose_name='如何進入房門', default='公司Key | 藏在現場 | 沒鎖 | 屋主開門', max_length=50)
	suite_include=models.CharField(verbose_name='租金包含', max_length=150, blank=True, null=True)
	suite_no_include=models.CharField(verbose_name='租金不包含', default='水:100/人 | 100/第2人 ,',max_length=100)
	suite_elecfee=models.CharField(verbose_name='電費計算', default='5元 | 台電,',max_length=10)
	suite_garbage=models.CharField(verbose_name='垃圾處理', default='公共 | 無', max_length=20)
	suite_wash=models.CharField(verbose_name='洗衣', default='獨立 | 公用 | 無', max_length=20)
	suite_drink=models.CharField(verbose_name='飲水', default='公共 | 無', max_length=20)
	suite_limit=models.CharField(verbose_name='限制條件', default='全部禁寵 | 部份禁寵:可貓 | 禁男',max_length=50)
	suite_note=models.TextField(verbose_name='其他補充', default=' ')
	class Meta:
		verbose_name_plural='套房案件'
	def __str__(self):
		return self.suite_address
	def get_absolute_url(self):
		return reverse('suite_detail', kwargs={'pk': self.pk})
	

class Rooms(models.Model):
	room_address=models.ForeignKey(Suites, on_delete=models.SET_NULL, blank=True, null=True, related_name='rooms')
	room_fullrent=models.BooleanField(verbose_name='可租狀態', default=True)
	room_number=models.CharField(verbose_name='房號', max_length=10, default='X')
	room_rent=models.PositiveIntegerField(verbose_name='價位', blank=True, null=True)
	room_description=models.CharField(verbose_name='其他優點', default=' ', blank=True, null=True, max_length=50)
	class Meta:
		verbose_name_plural='空屋資訊'
	"""
	def __str__(self):
		return self.room_number
	"""

#from filer.fields.image import FilerImageField

class SuitePhoto(models.Model):
	P_address=models.ForeignKey(Suites, on_delete=models.SET_NULL, blank=True, null=True, related_name='photo')
	p_subject = models.CharField(verbose_name='標題', max_length=100, blank=True, null=True)
	p_image = models.FileField(verbose_name='照片', upload_to='suite_photo/%Y-%m-%d', null=True, blank=True)
	#p_image = models.ImageField(verbose_name='上傳照片',upload_to='suite_photos', blank=True, null=True)
	#p_image = FilerImageField()
	p_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	class Meta:
		verbose_name_plural='照片'
	"""
	def __str__(self):
		return self.p_subject
	"""

