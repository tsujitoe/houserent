from django.contrib import admin

# Register your models here.
from .models import Suites, Rooms, SuitePhoto

class RoomInline(admin.StackedInline):
	model= Rooms
	extra = 1

class PhotoInline(admin.StackedInline):  
	model = SuitePhoto
	extra = 1

@admin.register(Suites)
class Suiteadmin(admin.ModelAdmin):
	search_fields = ('suite_address',)
	inlines = (RoomInline, PhotoInline, )
	list_per_page = 20


# admin.site.register(Suites)