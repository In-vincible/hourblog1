# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-06 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devohack', '0002_post_titleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gist',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]