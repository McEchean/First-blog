# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-27 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180327_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagpropertymodel',
            name='tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blogs.TagModel', verbose_name='标签'),
        ),
    ]
