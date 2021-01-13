from django.contrib import admin

from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "content", "creation_date")

admin.site.register(Posts, PostsAdmin)