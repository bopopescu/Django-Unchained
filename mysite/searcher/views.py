from django.core import serializers
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import *
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.views import generic

import psycopg2
import psycopg2.extras

from searcher.models import *

import json
import simplejson

import operator
import decimal
import datetime


class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
    	if hasattr(o, 'isoformat'):
           return o.isoformat()
        elif isinstance(o, decimal.Decimal):
            return str(o)
        return o.__dict__


def login_user(request):
	logout(request)
	username = password = ''
	
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/account/' + username)
	
	return render_to_response('searcher/login.html', context_instance=RequestContext(request))


@login_required(login_url='/login/')
def account_lookup(request, username):
	if request.is_ajax():
		envelope = {}

		try:
			user = list(User.objects.filter(username=username).values())
			checkings_account = list(user[0].CheckingsAccount.all())
			savings_account = list(user[0].SavingsAccount.all())

		except IndexError:
			envelope = {
				'status': 0,
				'message': 'not found'
			}

		else:

			data = {
				'user': user,
				'account': checkings_account,
				'account1': savings_account,
			}

			envelope = {
				'status': 1,
				'message': "1 okay",
				'data': data
			}

		return HttpResponse(simplejson.dumps(envelope, cls=DecimalJSONEncoder), content_type='application/json')

	else:	
		return render(request, 'searcher/account.html', {"username": username})

def close_account_form(request):
	if request.method == 'POST':
		form = CloseAccountForm(request.POST)

		print form

		if form.is_valid():

			print "Close account form is valid!"

			account_holder = form.cleaned_data['account_holder']
			debit_credit = form.cleaned_data['debit_credit']
			reason = form.cleaned_data['reason']

			account_close_request(account_holder, debit_credit, reason)

			return HttpResponse("Account closure request sent to banker. Account will close within 1 business day.")
	
	else: 
		form = CloseAccountForm()

	return render(request, 'searcher/close-form.html', {'form': form})


# Transfer Money form
# Tony 11/17/2014
def transfer_money_form(request):
	if request.method == 'POST':
		form = TransferMoneyForm(request.POST)

		print form

		if form.is_valid():

			print "Transfer form is valid!"

			account_holder = form.cleaned_data['account_holder']
			debit_credit = form.cleaned_data['debit_credit']
			reason = form.cleaned_data['reason']
			amount_transfer = form.cleaned_data['amount_transfer']
			routing_number= form.cleaned_data['routing_number']

			user_giving = Account.objects.filter(barcode=account_holder).get()
			user_receiving = Account.objects.filter(barcode=routing_number).get()

			user_giving_new_amount = user_giving.amount - amount_transfer

			# checking if the user who wants to transfer money has enough
			if user_giving_new_amount < 0:
				return HttpResponse("insufficient funds. Please place more money in account or transfer less")

			user_receiving_new_amount = user_receiving.amount + amount_transfer

			# updating new values after successful transfer
			user_giving.amount = user_giving_new_amount
			user_receiving.amount = user_receiving_new_amount

			user_giving.save()
			user_receiving.save()

			return HttpResponse("Money successfully transferred")
	
	else: 
		form = TransferMoneyForm()

	return render(request, 'searcher/transfer-form.html', {'form': form})






