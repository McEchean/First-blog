# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-29 09:07
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_tagmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxmodel',
            name='box_content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]
