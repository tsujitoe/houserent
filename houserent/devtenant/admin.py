from django.contrib import admin

# Register your models here.
from .models import Tenant


@admin.register(Tenant)
class Tenantifoadmin(admin.ModelAdmin):

	list_display = ('te_state', 'te_tracetime', 'te_name', 'te_phone', 'te_zone', 'te_money', 'te_date')
	fieldsets = (
		['Main',{
		'fields':('te_state', 'te_tracetime', 'te_name', 'te_phone'),
		}],
		['其他資訊',{
		'classes': ('collapse',),
		'fields':('te_note',),
		}]
	)
	search_fields = ('te_phone',)
	list_filter = ('te_state','te_zone','te_tracetime','te_date',)
	list_editable = ('te_state',)
	list_display_links = ('te_name',)
	list_per_page = 20
	#readonly_fields = ('image_tag',)