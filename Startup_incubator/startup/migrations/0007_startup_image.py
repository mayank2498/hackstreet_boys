# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-14 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0006_auto_20190214_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
