

from django.contrib import admin
from devstreet.models import Picture
#admin.site.register(Picture)

"""

from django import forms
from photologue.admin import GalleryAdmin as GalleryAdminDefault 
from photologue.models import Gallery


class GalleryAdminForm(forms.ModelForm):
	#Users never need to enter a description on a gallery.
	class Meta:
		model = Gallery
		exclude = ['description']

class GalleryAdmin(GalleryAdminDefault): 
	form = GalleryAdminForm

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
"""