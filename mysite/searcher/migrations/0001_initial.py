# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debit_credit', models.CharField(default=0, max_length=256)),
                ('amount', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=0, max_length=256)),
                ('address', models.CharField(default=0, max_length=256)),
                ('email', models.CharField(default=0, max_length=256)),
                ('barcode', models.CharField(default=0, max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
