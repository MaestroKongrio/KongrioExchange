# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.forms import ModelForm


# Create your models here.
class ExchangeAccount(models.Model):
	identification = models.CharField(max_length=20,unique=True)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=30,unique=True)

class ExchangeAccountForm(ModelForm):
	class Meta:
		model = ExchangeAccount
		fields = ['identification','name','address']


class Deposit(models.Model):
	account = models.ForeignKey(ExchangeAccount)
	amount = models.IntegerField()
	timestamp = models.DateTimeField(default=datetime.now,blank=True)

class Withdraw(models.Model):
	account = models.ForeignKey(ExchangeAccount)
	amount = models.IntegerField()
	timestamp = models.DateTimeField(default=datetime.now,blank=True)	
