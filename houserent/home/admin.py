from django.contrib import admin
from .models import HomeInfo, HomeMediaInfo, HomePhoto
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline



class PhotoInline(NestedStackedInline):  
	model = HomePhoto
	extra = 1
	#fields = ('image_tag',)
	readonly_fields = ('image_tag',)
	#exclude = ('h_image',)

@admin.register(HomeMediaInfo)
class HomeMediaInfoadmin(NestedModelAdmin):
	#search_fields = ('suite_address',)
	inlines = (PhotoInline, )
	list_per_page = 20

class HomeMediaInfoInline(NestedStackedInline):
	model = HomeMediaInfo
	extra = 1
	#readonly_fields = ('url_tag',)
	#exclude = ('home_title',)
	inlines = (PhotoInline, )


@admin.register(HomeInfo)
class HomeInfoadmin(NestedModelAdmin):
	inlines = (HomeMediaInfoInline, )
	list_per_page = 20

