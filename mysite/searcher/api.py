from django.db import models

from searcher.models import *
from datetime import datetime

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie import fields
from tastypie.exceptions import BadRequest

from rest_framework import serializers


#def account_close_request(account_holder, debit_credit, reason):
#	account_closing = CloseAccountRequest(account_holder=account_holder, debit_credit=debit_credit, reason=reason, date_requested=datetime.now())
#	account_closing.save()

