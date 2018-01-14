from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tenant(models.Model):
	state_items=(
		('新客', '新客'),
		('已租', '已租'),
		('可帶', '可帶'),
		('查詢', '查詢'),
		('無效', '無效'),
		('其他', '其他'),
	)

	te_state = models.CharField(verbose_name='狀態', choices=state_items, default='新打' ,max_length=20)
	te_date = models.DateField(verbose_name='更新時間', auto_now=True)
	te_name = models.CharField(verbose_name='姓名', blank=True, null=True, max_length=30)
	te_phone = models.CharField(verbose_name='電話', blank=True, null=True ,max_length=30)
	te_zone = models.CharField(verbose_name='想要區域', blank=True, null=True ,max_length=30)
	te_money = models.CharField(verbose_name='預算', blank=True, null=True ,max_length=30)
	te_note = models.TextField(verbose_name='房客紀錄', default='何時入住: ', blank=True, null=True)
	te_tracetime = models.DateField(verbose_name='追蹤時間', blank=True, null=True)
	class Meta:
		verbose_name_plural='房客資訊'
	def get_absolute_url(self):
		return reverse('tenant_list', kwargs={'pk': self.pk})
