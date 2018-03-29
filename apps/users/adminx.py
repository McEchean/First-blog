# -*-coding:utf-8-*-
__author__: 'McEachen'
__date__: '2018/3/26 17:14'

import xadmin
from .models import UserCommentModel, ContactModel
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '博客管理'
    site_footer = '我的博客'
    menu_style = 'accordion'


class UserProfileAdmin(object):
    list_display = ['nick_name', 'emial', 'image']
    search_fields = ['nick_name', 'emial', 'image']
    list_filter = ['nick_name', 'emial', 'image']


class UserCommentModelAdmin(object):
    list_display = ['user', 'comment', 'blog', 'add_time']
    search_fields = ['user', 'comment', 'blog']
    list_filter = ['user', 'comment', 'blog', 'add_time']


class ContactModelAdmin(object):
    list_display = ['user', 'suggest', 'add_time']
    search_fields = ['user', 'suggest']
    list_filter = ['user', 'suggest', 'add_time']


xadmin.site.register(UserCommentModel, UserCommentModelAdmin)
xadmin.site.register(ContactModel, ContactModelAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

