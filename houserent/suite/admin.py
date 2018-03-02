from django.contrib import admin
from .models import Suite, SuitePhotoInfo, SuitePhoto
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class PhotoInline(NestedStackedInline):  
	model = SuitePhoto
	extra = 1
	readonly_fields = ('image_tag',)

@admin.register(SuitePhotoInfo)
class SuitePhotoInfoadmin(NestedModelAdmin):
	inlines = (PhotoInline, )
	list_per_page = 20

class SuitePhotoInfoInline(NestedStackedInline):
	model = SuitePhotoInfo
	extra = 1
	inlines = (PhotoInline, )

@admin.register(Suite)
class Suiteadmin(NestedModelAdmin):
	search_fields = ('suite_address',)
	inlines = (SuitePhotoInfoInline, )
	list_per_page = 20
