from django.db import models
from django.core.urlresolvers import reverse #Django1.8.8
# Create your models here.

import pytesseract
from PIL import Image



class Devinfo(models.Model):
	state_items=(
		('未打', '未打'),
		('沒接', '沒接'),
		('追蹤', '追蹤'),
		('失敗', '失敗'),
		('成功', '成功'),
	)
	dev_date = models.DateField(verbose_name='搜集時間', auto_now_add=True)
	state = models.CharField(verbose_name='狀態', choices=state_items, default='未打' ,max_length=20)
	dev_url = models.CharField(verbose_name='網址', blank=True, null=True  ,max_length=100)
	dev_zone = models.CharField(verbose_name='區域', blank=True, null=True ,max_length=10)
	dev_address = models.CharField(verbose_name='地址', blank=True, null=True ,max_length=100)
	dev_rent = models.CharField(verbose_name='租金', blank=True, null=True ,max_length=50)
	dev_name = models.CharField(verbose_name='稱呼', blank=True, null=True ,max_length=30)
	dev_phone = models.CharField(verbose_name='電話', blank=True, null=True ,max_length=30)
	dev_phone_img = models.ImageField(verbose_name='電話圖', upload_to='dev-phone', null=True)
	dev_screenshot = models.ImageField(verbose_name='網頁截圖', upload_to='dev-phone', blank=True, null=True ,max_length=100)
	dev_note = models.TextField(verbose_name='開發紀錄', default=' ', blank=True, null=True)
	dev_tracetime = models.DateField(verbose_name='追蹤時間', blank=True, null=True)
	class Meta:
		verbose_name_plural='開發資訊'
	def image_tag(self):
		if self.dev_phone_img :
			return u'<img src="%s" width="100px" />' % self.dev_phone_img.url
	image_tag.short_description = '電話圖'
	image_tag.allow_tags = True

	def url_tag(self):
		if self.dev_url :
			return u'<a href="%s" target="_blank">#</a>' % self.dev_url
	url_tag.short_description = '連結'
	url_tag.allow_tags = True

	def image2number(self):
		#image = Image.open('phone-可伊-台中市北屯區文心路四段.png') #圖檔名稱
		image = Image.open("../media/%s"%(self.dev_phone_img))
		number = pytesseract.image_to_string(image)
		self.dev_phone=number


"""
	def dev_date_tag(self):	
		if self.dev_date :
			DATE_FORMAT = "%m-%d"
			return self.dev_date.strftime("%s" % (DATE_FORMAT))
	dev_date_tag.short_description = '搜集時間'
	dev_date_tag.allow_tags = True
"""
"""
	def dev_tracetime_tag(self):	
		if self.dev_tracetime :
			DATE_FORMAT = "%m-%d"
			return self.dev_tracetime.strftime("%s" % (DATE_FORMAT))
	dev_tracetime_tag.short_description = '搜集時間'
	dev_tracetime_tag.allow_tags = True
"""