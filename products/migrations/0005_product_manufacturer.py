# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-02 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.TextField(default=''),
        ),
    ]