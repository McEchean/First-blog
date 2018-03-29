# -*-coding:utf-8-*-
__author__: 'McEachen'
__date__: '2018/3/27 13:01'

import xadmin
from .models import TagPropertyModel


class TagPropertyModelAdmin(object):
    list_display = ['tag', 'blog', 'add_time']
    search_fields = ['tag', 'blog']
    list_filter = ['tag', 'blog', 'add_time']


xadmin.site.register(TagPropertyModel, TagPropertyModelAdmin)
