from django.contrib import admin

# Register your models here.
from .models import Devinfo


@admin.register(Devinfo)
class Dvenifoadmin(admin.ModelAdmin):

	list_display = ('state', 'dev_tracetime', 'dev_zone','dev_name','dev_phone',
		'dev_address','dev_rent', 'dev_date', 'screen_tag', 'url_tag',)
	fieldsets = (
		['Main',{
		'fields':('state','dev_menber' ,'dev_tracetime','dev_name', 'dev_phone', 'dev_note'),
		}],
		['其他資訊',{
		'classes': ('collapse',),
		'fields':('dev_source', 'dev_address', 'dev_rent',
			'dev_zone', 'dev_pattern', 
			'dev_phone_img','dev_screenshot_img','dev_screenshot_yes'),
		}]
	)
	search_fields = ('dev_phone','dev_address',)
	list_filter = ('state','dev_type', 'dev_zone','dev_date','dev_menber','dev_pattern', )
	list_editable = ('state',)
	list_display_links = ('dev_name',)
	list_per_page = 10
	#readonly_fields = ('image_tag',)