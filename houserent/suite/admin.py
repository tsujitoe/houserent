from django.contrib import admin

# Register your models here.
from .models import Suite, SuitePhoto


"""
class RoomInline(admin.StackedInline):
	model= Room
	extra = 1

class PhotoInline(admin.StackedInline):  
	model = SuitePhoto
	extra = 1

@admin.register(Suite)
class Suiteadmin(admin.ModelAdmin):
	search_fields = ('suite_address',)
	inlines = (RoomInline, PhotoInline, )
	list_per_page = 20
"""

# admin.site.register(Suites)