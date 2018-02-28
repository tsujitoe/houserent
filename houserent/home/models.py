from django.db import models
from multiselectfield import MultiSelectField
# my_field2 = MultiSelectField(choices=MY_CHOICES2, max_choices=3, max_length=3)

# Create your models here.

class HomeInfo(models.Model):
	manage_item=(
		('物管公司','物管公司'),
		('管理員','管理員'),
		('無','無'),
		('其他補充','其他補充'),
		)
	inter_item=(
		('公司Key','公司Key'),
		('屋主開門','屋主開門'),
		('管理室','管理室'),
		('密碼','密碼'),
		('其他補充','其他補充'),
		)
	include_items=(
		('水', '水'),
		('電', '電'),
		('網路', '網路'),
		('第四台', '第四台'),
		('垃圾費', '垃圾費'),
		('管理費', '管理費'),
		('其他', '其他'),
	)
	elecfee_item=(
		('台電','台電'),
		('5元','5元'),
		('4.5元','4.5元'),
		('4元','4元'),
		('其他補充','其他補充'),
		)
	garbage_item=(
		('社區集中','社區集中'),
		('子母車','子母車'),
		('自理','自理'),
		('其他補充','其他補充'),
		)


	pet_item=(
		('全部禁寵','全部禁寵'),
		('可寵','可寵'),
		('可貓','可貓'),
		('可狗','可狗'),
		('其他補充','其他補充'),
		)

	#基本資料
	home_address=models.CharField(verbose_name='案件地址', blank=True, null=True ,max_length=60)
	home_master=models.CharField(verbose_name='房東姓名', blank=True, null=True ,max_length=20)
	home_master_phone=models.CharField(verbose_name='房東電話', blank=True, null=True ,max_length=20)
	home_how_manage=models.CharField(verbose_name='管理方式', choices=manage_item , default='無', max_length=20)
	home_how_inter_door=models.CharField(verbose_name='如何進入房門', choices=inter_item, default='公司Key', max_length=50)
	#租金細目
	#home_include=models.CharField(verbose_name='租金包含', max_length=150, blank=True, null=True)
	home_no_include=MultiSelectField(verbose_name='租金不包含',choices=include_items, default='測試', max_length=100)
	home_elecfee=models.CharField(verbose_name='電費計算', choices=elecfee_item, default='台電', max_length=20)
	home_garbage=models.CharField(verbose_name='垃圾處理', choices=garbage_item, default='公共', max_length=20)
	#設備包含
	home_wash=models.CharField(verbose_name='洗衣', default='獨立 | 公用 | 無', max_length=20)
	home_drink=models.CharField(verbose_name='飲水', default='公共 | 無', max_length=20)
	#條件限制與補充
	home_pet=models.CharField(verbose_name='寵物限制', choices=pet_item, default='全部禁寵',max_length=20)
	home_limit=models.CharField(verbose_name='其他限制', default='禁男 | 禁女 | 年紀限制：',max_length=50)
	home_note=models.TextField(verbose_name='其他補充', default=' ')
	class Meta:
		verbose_name_plural='住宅案件'
	def __str__(self):
		return self.home_address

	#def get_absolute_url(self):
	#	return reverse('suite_detail', kwargs={'pk': self.pk})






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

