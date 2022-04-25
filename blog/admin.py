from django.contrib import admin
from .models import Post, Tags, Comments

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    # prepopulated_fields = {'slug': ('title',)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('content',)