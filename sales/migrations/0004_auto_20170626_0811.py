# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20170626_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='sale_order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]