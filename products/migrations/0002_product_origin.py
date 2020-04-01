# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-01 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
