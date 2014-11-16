from django.db import models


class User(models.Model):
	name = models.CharField(max_length=256, default = 0)
	address = models.CharField(max_length=256, default = 0)
	email = models.CharField(max_length=256, default = 0)
	barcode = models.CharField(max_length=256, default = 0)

class Account(models.Model):
	debit_credit = models.CharField(max_length=256, default = 0)
	amount = models.DecimalField(default = 0, max_digits=10, decimal_places=2)
	barcode = models.CharField(max_length=256, default = 0)