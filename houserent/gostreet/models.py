from django.db import models
from django.core.urlresolvers import reverse
#from slugify import slugify

class MediaInfo(models.Model):
	state_items=(
		('新接', '新接'),
		('屋主', '屋主'),
		('查詢', '查詢'),
		('拜訪', '拜訪'),
		('失敗', '失敗'),
		('成功', '成功'),
	)
	type_items=(
		('店面', '店面'),
		('套房', '套房'),
		('住宅', '住宅'),
		('其他', '其他'),
	)

	now_state = models.CharField(verbose_name='狀態', choices=state_items, default='新接' ,max_length=20)
	now_type = models.CharField(verbose_name='類型', choices=type_items, default='新接' ,max_length=20)
	now_address = models.CharField(verbose_name='場勘地址', blank=True, null=True, max_length=100)
	now_phone = models.CharField(verbose_name='現場電話', blank=True, null=True, max_length=30)
	now_note = models.TextField(verbose_name='紀錄備忘', default='租金價位: \n是否仲介: \n其他注意:', blank=True, null=True)

	#謄本資料
	now_transcript_name = models.CharField(verbose_name='所有權人', blank=True, null=True, max_length=50)
	now_transcript_address = models.CharField(verbose_name='戶籍地址', blank=True, null=True, max_length=100)
	now_transcript_note = models.TextField(verbose_name='查詢記錄', default='.', blank=True, null=True)

	#時間追蹤
	now_date = models.DateField(verbose_name='更新時間', auto_now=True)
	now_tracetime = models.DateField(verbose_name='追蹤時間', blank=True, null=True)

	class Meta:
		verbose_name_plural='掃街資訊'

	def get_absolute_url(self):
		return reverse('detail_street', kwargs={'pk': self.pk})
	def get_absolute_url_edit(self):
		return reverse('update_street', kwargs={'pk': self.pk})
	def url_tag(self):
		return u'<a href="%s" target="_blank">Go</a>' % self.get_absolute_url_edit
	url_tag.short_description = '修正'
	url_tag.allow_tags = True


	
class Media(models.Model):
	media_files = models.ForeignKey(MediaInfo, on_delete=models.SET_NULL, blank=True, null=True, related_name='img_address')
	image = models.ImageField(verbose_name='', upload_to='street_photo/%Y-%m-%d', blank=True, null=True)
	image_note = models.CharField(verbose_name='照片說明', default='.',blank=True, null=True, max_length=50)
	def __str__(self):
		return '圖片'

	def image_tag(self):
		if self.image :
			return u'<img src="%s" width="100px" />' % self.iamge.url
	image_tag.short_description = '圖片'
	image_tag.allow_tags = True



class FakeInfo(models.Model):
	state_items=(
		('未打', '未打'),
		('收養', '收養'),
		('完成', '完成'),
	)

	fake_date = models.DateField(verbose_name='建立時間', auto_now_add=True)
	fake_state = models.CharField(verbose_name='狀態', choices=state_items, default='未打' ,max_length=20)
	fake_tenant = models.CharField(verbose_name='認養人', blank=True, null=True, max_length=20)
	fake_url = models.CharField(verbose_name='網址', blank=True, null=True, max_length=100)
	fake_source = models.CharField(verbose_name='來源', blank=True, null=True, max_length=20)
	fake_zone = models.CharField(verbose_name='區域', blank=True, null=True ,max_length=10)
	#fake_pattern = models.CharField(verbose_name='格局', blank=True, null=True ,max_length=30)
	fake_address = models.CharField(verbose_name='網路地址', blank=True, null=True ,max_length=100)
	fake_real_address = models.CharField(verbose_name='真實地址', blank=True, null=True ,max_length=100)
	fake_rent = models.CharField(verbose_name='租金', blank=True, null=True ,max_length=50)
	fake_name = models.CharField(verbose_name='稱呼', blank=True, null=True ,max_length=30)
	#fake_phone = models.CharField(verbose_name='電話', blank=True, null=True ,max_length=30)
	fake_phone_img = models.ImageField(verbose_name='電話圖', upload_to='dev-phone', blank=True, null=True)
	fake_screenshot_img = models.ImageField(verbose_name='網頁截圖', upload_to='dev-web', blank=True, null=True ,max_length=100)
	fake_note = models.TextField(verbose_name='開發紀錄', default=' ', blank=True, null=True)
	fake_tracetime = models.DateField(verbose_name='追蹤時間', blank=True, null=True)

	#謄本資料
	fake_transcript_name = models.CharField(verbose_name='所有權人', blank=True, null=True, max_length=50)
	fake_transcript_address = models.CharField(verbose_name='戶籍地址', blank=True, null=True, max_length=100)
	fake_transcript_note = models.TextField(verbose_name='查詢記錄', default='.', blank=True, null=True)


	class Meta:
		verbose_name_plural='假房搜集'
	def url_tag(self):
		if self.fake_url :
			return u'<a href="%s" target="_blank">Go</a>' % self.fake_url
	url_tag.short_description = '連結'
	url_tag.allow_tags = True
	def image_tag(self):
		if self.fake_phone_img :
			return u'<img src="%s" width="100px" />' % self.fake_phone_img.url
	image_tag.short_description = '電話圖'
	image_tag.allow_tags = True



"""
# Create your models here.
class Post(models.Model):
	street_title = models.CharField(blank=True, null=True, max_length=100)
	#body = models.CharField(max_length=400)

def get_image_filename(instance, filename):
	title = instance.post.title
	slug = slugify(title)
	return "post_images/%s-%s" % (slug, filename)  


class Images_street(models.Model):
	img_street = models.ForeignKey(Post, verbose_name='案件地址', on_delete=models.SET_NULL, blank=True, null=True, related_name='img_street')
	image = models.ImageField(upload_to=get_image_filename, verbose_name='掃街照片', blank=True, null=True )
"""
