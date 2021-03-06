from django.db import models


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

	type_items=(
		('套房', '套房'),
		('住宅', '住宅'),
		('店面', '店面'),
		('其他', '其他'),
	)


	te_state = models.CharField(verbose_name='狀態', choices=state_items, default='新打' ,max_length=20)
	te_type =  models.CharField(verbose_name='案件類型', choices=type_items, default='套房' ,max_length=20)
	te_member = models.CharField(verbose_name='負責同仁', blank=True, null=True, max_length=30)
	te_tracetime = models.DateField(verbose_name='追蹤時間', blank=True, null=True)
	te_up_date = models.DateField(verbose_name='更新時間', auto_now=True)

	te_name = models.CharField(verbose_name='姓名', blank=True, null=True, max_length=30)
	te_phone = models.CharField(verbose_name='電話', blank=True, null=True ,max_length=30)
	te_zone = models.CharField(verbose_name='想要區域', blank=True, null=True ,max_length=30)
	te_money = models.CharField(verbose_name='預算', blank=True, null=True ,max_length=30)
	te_in_date = models.DateField(verbose_name='何時入住', blank=True, null=True )
	te_note = models.TextField(verbose_name='房客紀錄', default='何時入住: \n預算多少: \n其他需求:', blank=True, null=True)
	
	class Meta:
		verbose_name_plural='房客資訊'
	