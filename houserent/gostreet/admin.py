from django.contrib import admin

from .models import MediaInfo, Media, FakeInfo
from .forms import AdminImageWidget, MediaForm

from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.

class ImageInline(AdminImageMixin, admin.TabularInline):
  model = Media
  form  = MediaForm
  extra = 1

"""
class MediaInline(admin.StackedInline):
	model = Media
	#fields = ('image_tag',)
	extra = 1
"""

@admin.register(MediaInfo)
class MediaInfoadmin(AdminImageMixin, admin.ModelAdmin):
	search_fields = ('now_address', 'now_phone',)
	list_display = ('now_state', 'now_type', 'now_tracetime', 'now_address', 'now_phone', 'now_date',)
	list_editable = ('now_state',)
	list_display_links = ('now_address',)
	list_filter = ('now_tracetime',)
	list_per_page = 10
	inlines = (ImageInline, )
	fieldsets = (
		['Main',{
		'fields':('now_state', 'now_tracetime', 'now_address', 'now_phone'),
		}],
		['謄本資訊',{
		'classes': ('collapse',),
		'fields':('now_transcript_name', 'now_transcript_address', 'now_transcript_note'),
		}]
	)


@admin.register(FakeInfo)
class FakeInfoadmin(admin.ModelAdmin):
	search_fields = ('fake_address', 'fake_real_address', )
	list_display = ('fake_state', 'fake_tracetime', 'fake_zone','fake_name','image_tag',
		'fake_address',  'fake_rent', 'fake_date', 'url_tag', 'fake_real_address',)
	list_editable = ('fake_state',)
	list_display_links = ('fake_name',)
	list_filter = ('fake_state', 'fake_tracetime', 'fake_zone', 'fake_tracetime', 'fake_date', 'fake_tenant',)
	list_per_page = 10
	fieldsets = (
		['Main',{
		'fields':('fake_state', 'fake_tracetime', 'fake_address', 'fake_phone_img',
			'fake_tenant', 'fake_real_address', 'fake_note', ),
		}],
		['謄本資訊',{
		'classes': ('collapse',),
		'fields':('fake_transcript_name', 'fake_transcript_address', 'fake_transcript_note'),
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