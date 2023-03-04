from django.db import models
from PIL import Image
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.dispatch import receiver
# Create your models here.

##Category Model##
class Categories(models.Model):
    catId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    addedDate = models.DateTimeField(auto_now_add=True,null=True)

    ##to display image in admin site
    def image_tag(self):
        return format_html('<img src = "/media/{}" style = "width: 40px; height: 40px; border-radius:50%">'.format(self.image))

    def __str__(self):
        return self.title


##POST MODEL##

class Posts(models.Model):
    postId= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    addedDate = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src = "/media/{}" style = "width: 40px; height: 40px">'.format(self.image))


    def __str__(self):
        return self.title