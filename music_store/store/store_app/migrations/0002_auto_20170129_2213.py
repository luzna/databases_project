# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_item',
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(default=None, blank=True, to='store_app.Order', null=True),
        ),
    ]
