# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='barcode',
            field=models.CharField(default=0, max_length=256),
            preserve_default=True,
        ),
    ]
