# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-12 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20190110_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='user_id',
            new_name='user',
        ),
    ]
