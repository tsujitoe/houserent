from django.contrib import admin

# Register your models here.
from .models import Tenant


@admin.register(Tenant)
class Tenantifoadmin(admin.ModelAdmin):

	list_display = ('te_tracetime', 'te_state', 'te_type', 'te_member',
		'te_name', 'te_phone', 'te_zone', 'te_money', 'te_in_date')
	fieldsets = (
		['Main',{
		'fields':('te_tracetime', 'te_state', 'te_type', 'te_member',
			'te_name', 'te_phone', 'te_zone', 'te_money', 'te_in_date'),
		}],
		['其他資訊紀錄',{
		'fields':('te_note',),
		}]
	)
	search_fields = ('te_phone',)
	list_filter = ('te_member', 'te_type', 'te_state','te_zone','te_tracetime','te_in_date', )
	list_editable = ('te_state',)
	list_display_links = ('te_name',)
	list_per_page = 10
	#readonly_fields = ('image_tag',)

