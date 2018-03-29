"""Blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blogs.views import HomepageView
from blogs.views import ContactView, SuggestView
from django.views.static import serve
import xadmin
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',HomepageView.as_view(),name='homepage'),


    #配置blogs的url
    url(r'^blogs/',include('blogs.urls',namespace='blogs')),
    #contact的url
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^add_suggest/$',SuggestView.as_view(),name= 'add_suggest'),


    #配置media的url
    url(r'^media/(?P<path>.*)$',serve,{'document_root': MEDIA_ROOT}),

    # 添加富文本url
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
