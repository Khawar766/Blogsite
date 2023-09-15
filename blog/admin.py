from django.contrib import admin
from .models import Blogpost,Blogcomment

admin.site.register(Blogcomment)
@admin.register(Blogpost)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('jsfiles/tinyplugin.js',)