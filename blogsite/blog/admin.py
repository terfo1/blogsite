from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)
    ordering = ('-published_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_name', 'created_date')
    search_fields = ('author_name', 'comment_text')
    list_filter = ('created_date',)
    ordering = ('-created_date',)
