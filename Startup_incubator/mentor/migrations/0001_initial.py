# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-15 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=10000, null=True)),
                ('image', models.FileField(default='profile_photos/default.jpg', upload_to='profile_photos/')),
            ],
        ),
    ]
