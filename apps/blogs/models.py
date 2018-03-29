from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.


class CategoryModel(models.Model):
    Theme_name = models.CharField(max_length=50,verbose_name=u'主题名称')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Theme_name


class BlogModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    category = models.ForeignKey(CategoryModel, verbose_name=u'类别')
    content = RichTextField(verbose_name=u'内容')
    desc = models.CharField(max_length=100, verbose_name=u'简述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BoxModel(models.Model):
    box_title = models.CharField(max_length=50, verbose_name=u'box名')
    box_image = models.ImageField(upload_to='box/%Y/%m', max_length=2000, verbose_name=u'box图片')
    box_content = RichTextField(verbose_name=u'box内容')
    # box_content = models.TextField(verbose_name=u'box内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'box'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.box_title


class TagModel(models.Model):
    tag_name = models.CharField(max_length=10,verbose_name=u'标签')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name



