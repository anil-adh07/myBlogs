from django.contrib import admin
from .models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=('catId','title','url','image_tag','addedDate')
    list_filter =('title',)



    
class postAdmin(admin.ModelAdmin):
    list_display=('postId','title','url',)


admin.site.register(Categories,categoryAdmin)
admin.site.register(Posts,postAdmin)