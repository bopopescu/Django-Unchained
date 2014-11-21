from django.contrib import admin
from searcher.models import *

admin.site.register(User)
admin.site.register(CheckingsAccount)
admin.site.register(SavingsAccount)
admin.site.register(CheckingsTransaction)
admin.site.register(SavingsTransaction)