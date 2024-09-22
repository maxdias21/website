from django.contrib import admin
from .models import PostBlog
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'content')
    list_display = ('id', 'title', 'author', 'is_published')
    list_display_links = ('id', 'title')
    list_per_page = 10
    list_editable = ('is_published',)


admin.site.register(PostBlog, BlogAdmin)
