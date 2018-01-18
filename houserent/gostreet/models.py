from django.db import models
from django.core.urlresolvers import reverse
#from slugify import slugify

def get_image_filename(instance, filename):
	#title = instance.media_files.now_address
	#slug = slugify(title)
	return "street_images/掃街照片-%s" % (filename)  


class MediaInfo(models.Model):
	now_address = models.CharField(verbose_name='場勘地址', blank=True, null=True, max_length=100)
	now_phone = models.CharField(verbose_name='現場電話', blank=True, null=True, max_length=30)
	now_note = models.TextField(verbose_name='紀錄備忘', default='租金價位: \n是否仲介: \n其他注意:', blank=True, null=True)
	def get_absolute_url(self):
		return reverse('detail_street', kwargs={'pk': self.pk})
	
class Media(models.Model):
	media_files = models.ForeignKey(MediaInfo, verbose_name='現場照片',on_delete=models.SET_NULL, blank=True, null=True, related_name='img_address')
	image = models.FileField(upload_to=get_image_filename)



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
