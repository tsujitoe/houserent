from django.contrib import admin
from .models import StoreInfo, StoreMediaInfo, StorePhoto
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class PhotoInline(NestedStackedInline):  
	model = StorePhoto
	extra = 1
	#fields = ('image_tag',)
	readonly_fields = ('image_tag',)
	#exclude = ('h_image',)

@admin.register(StoreMediaInfo)
class StoreMediaInfoadmin(NestedModelAdmin):
	#search_fields = ('suite_address',)
	inlines = (PhotoInline, )
	list_per_page = 20

class StoreMediaInfoInline(NestedStackedInline):
	model = StoreMediaInfo
	extra = 1
	#readonly_fields = ('url_tag',)
	#exclude = ('home_title',)
	inlines = (PhotoInline, )


@admin.register(StoreInfo)
class StoreInfoadmin(NestedModelAdmin):
	inlines = (StoreMediaInfoInline, )
	list_per_page = 20

