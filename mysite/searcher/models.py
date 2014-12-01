from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UserProfile(models.Model):
	user = models.ForeignKey(User)

class CorporateUser(models.Model):
	profile = models.ForeignKey(UserProfile)


class IndividualUser(models.Model):
	profile = models.ForeignKey(UserProfile)

	name = models.CharField(max_length=256, default = 0)
	address = models.CharField(max_length=256, default = 0)
	birthday = models.CharField(max_length=256, default=0)
	email = models.CharField(max_length=256, default = 0)


class CheckingsAccount(models.Model):
	user = models.ForeignKey(User)
	amount = models.DecimalField(default = 0, max_digits=10, decimal_places=2)

class SavingsAccount(models.Model):
	user=models.ForeignKey(User)
	amount = models.DecimalField(default = 0, max_digits=10, decimal_places=2)


class TransactionBarcodeSeq(models.Model):
	placeholder = models.CharField(max_length=8)

class CheckingsTransaction(models.Model):
	account = models.ForeignKey(CheckingsAccount)
	date = models.DateTimeField(auto_now_add=True)
	amount_moved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	description = models.CharField(max_length=256, default=0)
	barcode = models.CharField(max_length = 8)


class SavingsTransaction(models.Model):
	account = models.ForeignKey(SavingsAccount)
	date = models.DateTimeField(auto_now_add=True)
	amount_moved = models.DecimalField(default=0, max_digits=10, decimal_places=2)
	description = models.CharField(max_length=256, default=0)
	barcode = models.CharField(max_length = 8)


@receiver(pre_save, sender=CheckingsTransaction)
def get_checkings_transaction_barcode(sender, instance, *args, **kwargs):
  if instance.barcode == '':                                                          
    seq = TransactionBarcodeSeq.objects.create()                            
    instance.barcode = "BCT{0:05d}".format(seq.id)

@receiver(pre_save, sender=SavingsTransaction)
def get_savings_transaction_barcode(sender, instance, *args, **kwargs):
  if instance.barcode == '':                                                          
    seq = TransactionBarcodeSeq.objects.create()                            
    instance.barcode = "BST{0:05d}".format(seq.id)


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