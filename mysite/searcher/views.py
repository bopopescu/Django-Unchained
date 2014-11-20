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
				return HttpResponseRedirect('/account/100')
	
	return render_to_response('searcher/login.html', context_instance=RequestContext(request))


#@login_required(login_url='/login/')
def account_lookup(request, barcode):
	if request.is_ajax():
		envelope = {}

		try:
			user = list(User.objects.filter(barcode=barcode).values())
			account = list(Account.objects.filter(barcode=barcode).values())

		except IndexError:
			envelope = {
				'status': 0,
				'message': 'not found'
			}

		else:

			data = {
				'user': user,
				'account': account
			}

			envelope = {
				'status': 1,
				'message': "1 okay",
				'data': data
			}

		return HttpResponse(simplejson.dumps(envelope, cls=DecimalJSONEncoder), content_type='application/json')

	else:
		return render(request, 'searcher/account.html', {"barcode": barcode})




