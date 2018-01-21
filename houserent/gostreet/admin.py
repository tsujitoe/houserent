from django.contrib import admin


from .models import MediaInfo, Media
# Register your models here.

class MediaInline(admin.StackedInline):
	model = Media
	#fields = ('image_tag',)
	extra = 1

@admin.register(MediaInfo)
class MediaInfoadmin(admin.ModelAdmin):
	search_fields = ('now_address',)
	list_display = ('now_state', 'now_address', 'now_phone',)
	list_editable = ('now_state',)
	list_display_links = ('now_address',)
	list_per_page = 10
	inlines = (MediaInline, )
	fieldsets = (
		['Main',{
		'fields':('now_state', 'now_address', 'now_phone'),
		}],
		['其他資訊',{
		'classes': ('collapse',),
		'fields':(),
		}]
	)


"""
from .models import Post, Images_street
# Register your models here.

class ImageInline(admin.StackedInline):
	model= Images_street
	#extra = 3

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
	#search_fields = ('suite_address',)
	inlines = (ImageInline, )
	list_per_page = 10
"""