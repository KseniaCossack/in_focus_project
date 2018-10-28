from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib import admin

from .fields import ThumbnailImageField

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()


    class Meta:
        ordering = ['name']
   
    def __unicode__(self):
        return self.name


   # @permalink    
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})

class Photo(models.Model):
    item = models.ForeignKey(Item, on_delete= False)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

   # @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})


class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo) 


# Create your models here.
