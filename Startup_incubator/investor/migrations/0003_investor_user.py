# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-14 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('investor', '0002_investor_startups'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Type'),
        ),
    ]