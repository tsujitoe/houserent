from django.contrib import admin

# Register your models here.
from .models import Devinfo


@admin.register(Devinfo)
class Dvenifoadmin(admin.ModelAdmin):

	list_display = ('state', 'dev_tracetime', 'dev_type', 'dev_zone','dev_name','dev_phone', 'image_tag',
		'dev_address','dev_rent', 'dev_date', 'screen_tag', 'url_tag',)
	fieldsets = (
		['Main',{
		'fields':('state', 'dev_tracetime','dev_name', 'dev_phone','dev_phone_img'),
		}],
		['其他資訊',{
		'classes': ('collapse',),
		'fields':('dev_note', 'dev_address','dev_rent', 'dev_screenshot_img'),
		}]
	)
	search_fields = ('dev_phone',)
	list_filter = ('state','dev_type','dev_zone','dev_date',)
	list_editable = ('state',)
	list_display_links = ('dev_name',)
	list_per_page = 10
	#readonly_fields = ('image_tag',)
