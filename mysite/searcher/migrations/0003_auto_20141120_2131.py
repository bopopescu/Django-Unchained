# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0002_account_barcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckingsAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('user', models.ForeignKey(to='searcher.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CheckingsTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount_moved', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('description', models.CharField(default=0, max_length=256)),
                ('barcode', models.CharField(max_length=8)),
                ('account', models.ForeignKey(to='searcher.CheckingsAccount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CloseAccountRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_holder', models.CharField(default=0, max_length=256)),
                ('debit_credit', models.CharField(default=0, max_length=256)),
                ('reason', models.CharField(default=0, max_length=256)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('user', models.ForeignKey(to='searcher.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SavingsTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount_moved', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('description', models.CharField(default=0, max_length=256)),
                ('barcode', models.CharField(max_length=8)),
                ('account', models.ForeignKey(to='searcher.SavingsAccount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransactionBarcodeSeq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeholder', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='account',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='barcode',
            new_name='birthday',
        ),
    ]
