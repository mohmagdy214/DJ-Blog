from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['draft','author']
    search_fields = ['title','content']

class CommentAdmin(admin.ModelAdmin):  
    list_display = ['user','post','created_at']
    list_filter = ['user']



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)