from django.contrib import admin
from .models import Post, Image

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('created',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}

class ImageAdmin(admin.ModelAdmin):
    search_fields = ('attached_to__slug',)

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
