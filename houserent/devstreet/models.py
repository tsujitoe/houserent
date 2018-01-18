from django.db import models


class GoStreet(models.Model):
    street =  models.CharField(verbose_name='地址', blank=True, null=True ,max_length=100)


class Picture(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    #不知道該怎麼加進去QQ
    #street =models.ForeignKey(GoStreet, on_delete=models.SET_NULL, blank=True, null=True, related_name='street')
    title = models.CharField(verbose_name='照片說明', blank=True, null=True ,max_length=60)
    file = models.ImageField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)

    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
