from django.contrib import admin


from .models import MediaInfo, Media
# Register your models here.

class MediaInline(admin.StackedInline):
	model= Media
	extra = 1

@admin.register(MediaInfo)
class MediaInfoadmin(admin.ModelAdmin):
	#search_fields = ('suite_address',)
	inlines = (MediaInline, )
	list_per_page = 10


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