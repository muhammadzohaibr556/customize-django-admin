from django.db import models
from django.template.defaultfilters import truncatechars 
from django.utils.safestring import mark_safe
# Create your models here.

class DemoProfile(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='photos')
    publish_date = models.DateTimeField(auto_now_add=True,editable=False)

    # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="200" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name
    

class CalculateField(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return str(self.a)