from django.contrib import admin

from .models import Blog, Comment, Category, Tag

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
