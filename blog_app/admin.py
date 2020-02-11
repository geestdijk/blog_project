from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', "published_date", "updated_at")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)