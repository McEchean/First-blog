from django.db import models
from datetime import datetime

from blogs.models import BlogModel, TagModel

# Create your models here.


class TagPropertyModel(models.Model):
    tag = models.ForeignKey(TagModel,verbose_name=u'标签',default='')
    blog = models.ForeignKey(BlogModel,verbose_name=u'博客',default='')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'标签属性'
        verbose_name_plural = verbose_name


