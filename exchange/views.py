# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from exchange.models import *

# Create your views here.
def exchange_home(request):
	return render(request,"home.html")

def exchange_add_account(request):
	return render_to_response('add_account.html', {'form': ExchangeAccountForm})