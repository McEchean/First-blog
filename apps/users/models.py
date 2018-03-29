from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from blogs.models import BlogModel


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=10, verbose_name=u'昵称')
    emial = models.EmailField(max_length=50, verbose_name=u'邮箱')
    image = models.ImageField(upload_to='users/%Y/%m', null=True, blank=True, verbose_name=u'用户头像')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class UserCommentModel(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    comment = models.CharField(max_length=400, null=True, blank=True, verbose_name=u'评论')
    blog = models.ForeignKey(BlogModel, verbose_name=u'博客')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户评论'
        verbose_name_plural = verbose_name


class ContactModel(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    suggest = models.TextField(verbose_name=u'建议或意见')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户建议'
        verbose_name_plural = verbose_name
