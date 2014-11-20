from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(models.Model):
	name = models.CharField(max_length=256, default = 0)
	address = models.CharField(max_length=256, default = 0)
	birthday = models.CharField(max_length=256, default=0)
	email = models.CharField(max_length=256, default = 0)

class Account(models.Model):
	user = models.ForeignKey(User)
	debit_credit = models.CharField(max_length=256, default = 0)
	amount = models.DecimalField(default = 0, max_digits=10, decimal_places=2)

class Transaction(models.Model):
	account = models.ForeignKey(Account)
	date = models.DateTimeField(auto_now_add=True)
	amount_moved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	description = models.CharField(max_length=256, default=0)


class CloseAccountRequest(models.Model):
	account_holder = models.CharField(max_length=256, default=0)
	debit_credit = models.CharField(max_length=256, default = 0)
	reason = models.CharField(max_length=256, default=0)
	date_requested = models.DateTimeField(auto_now_add=True)


class CloseAccountForm(forms.Form):
	account_holder = forms.CharField(max_length=256)
	debit_credit = forms.CharField(max_length=256)
	reason = forms.CharField(max_length=256)

class TransferMoneyForm(forms.Form):
	account_holder = forms.CharField(max_length=256)
	debit_credit = forms.CharField(max_length=256)
	reason = forms.CharField(max_length=256)
	amount_transfer = forms.DecimalField(max_digits=10, decimal_places=2)
	routing_number = forms.CharField(max_length=256)