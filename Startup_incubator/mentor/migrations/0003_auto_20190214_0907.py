# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-14 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_auto_20190214_0906'),
        ('mentor', '0002_mentor_startups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='startups',
        ),
        migrations.AddField(
            model_name='mentor',
            name='startups',
            field=models.ManyToManyField(blank=True, null=True, to='startup.Startup'),
        ),
    ]