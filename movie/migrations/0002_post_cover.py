# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-06 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='', upload_to=b'', verbose_name='\u56fe\u7247'),
            preserve_default=False,
        ),
    ]