# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Tag, Category, Author
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('postTitle',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('tagTitle',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('categoryTitle',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
