from django.db import models

# Create your models here.

class HomeInfo(models.Model):
	home_address=models.CharField(verbose_name='案件地址', blank=True, null=True ,max_length=60)
	class Meta:
		verbose_name_plural='住宅案件'
	def __str__(self):
		return self.home_address


class HomeMediaInfo(models.Model):
	home_address=models.ForeignKey(HomeInfo, on_delete=models.SET_NULL, blank=True, null=True, related_name='rooms')
	home_title=models.CharField(verbose_name='標題' ,max_length=60)
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

