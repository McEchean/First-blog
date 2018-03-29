# -*-coding:utf-8-*-
__author__: 'McEachen'
__date__: '2018/3/26 17:10'

import xadmin

from .models import BlogModel, BoxModel, CategoryModel, TagModel
from operation.models import TagPropertyModel

class TagInline(object):
    model = TagPropertyModel
    extra = 0

class BlogInline(object):
    model = BlogModel
    extra = 0

class BlogModelAdmin(object):
    # style_fields = {"detail": "ueditor"}
    list_display = ['title', 'category', 'content', 'desc', 'add_time']
    search_fields = ['title', 'category', 'content', 'desc']
    list_filter = ['title', 'category', 'content', 'desc', 'add_time']
    inlines = [TagInline]


class BoxModelAdmin(object):
    list_display = ['box_title', 'box_image', 'box_content', 'add_time']
    search_fields = ['box_title', 'box_image', 'box_content']
    list_filter = ['box_title', 'box_image', 'box_content', 'add_time']


class CategoryModelAdmin(object):
    list_display = ['Theme_name', 'add_time']
    search_fields = ['Theme_name']
    list_filter = ['Theme_name', 'add_time']
    inlines = [BlogInline]


class TagModelAdmin(object):
    list_display = ['tag_name', 'add_time']
    search_fields = ['tag_name']
    list_filter = ['tag_name', 'add_time']


xadmin.site.register(BlogModel, BlogModelAdmin)
xadmin.site.register(BoxModel, BoxModelAdmin)
xadmin.site.register(CategoryModel, CategoryModelAdmin)
xadmin.site.register(TagModel, TagModelAdmin)

