# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name;

class Term(models.Model):
    type = models.CharField(max_length=10) # monthly, quarterly, or annually.
    def __unicode__(self):
        return self.type;

class Plan(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    count = models.IntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE)