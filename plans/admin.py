# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Provider, Term, Plan, Cart, CartItem

admin.site.register(Provider)
admin.site.register(Term)
admin.site.register(Plan)
admin.site.register(Cart)
admin.site.register(CartItem)

# Register your models here.
