#-*-coding:utf-8-*-
__author__: 'McEachen'
__date__: '2018/3/26 17:36'

from django.conf.urls import url
from .views import BlogHomepageView,BlogDetailView,AddCommentView, BoxView, ContactView, SuggestView

urlpatterns = [
    url(r'^homepage/$',BlogHomepageView.as_view(),name='blog_homepage'),
    url(r'^box/$',BoxView.as_view(),name='box'),
    url(r'^blog_detail/(?P<blog_id>\d+)/$',BlogDetailView.as_view(),name= 'blog_detail'),
    url(r'^add_comment/(?P<blog_id>\d+)/$',AddCommentView.as_view(),name= 'add_comment'),

]