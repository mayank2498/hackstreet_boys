# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-14 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_incubation_startup'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='clicked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='incubation',
            name='clicked',
            field=models.BooleanField(default=False),
        ),
    ]
