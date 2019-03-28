# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from .models import Cart, CartItem, Provider, Term, Plan
from rest_framework import viewsets, response, status
from plans.serializers import UserSerializer, GroupSerializer, CartSerializer, CartItemSerializer, ProviderSerializer, TermSerializer, PlanSerializer
from django.http import HttpResponse, HttpResponseForbidden

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        parent = Cart.objects.get(id=request.data['cart'])
        if (parent.paid == 1):
            return response.Response("You cannot modify a paid cart", status.HTTP_400_BAD_REQUEST)
        return super(CartItemViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        parent = Cart.objects.get(id=request.data['cart'])
        if (parent.paid == 1):
            return response.Response("You cannot modify a paid cart", status.HTTP_400_BAD_REQUEST)
        return super(CartItemViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object();
        parent = Cart.objects.get(id=instance.cart_id)
        if (parent.paid == 1):
            return response.Response("You cannot modify a paid cart", status.HTTP_400_BAD_REQUEST)
        return super(CartItemViewSet, self).destroy(request, *args, **kwargs)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

def manual_payment(request, id):
    items = CartItem.objects.filter(cart_id = id)
    print(items)
    if (len(items) < 1):
        return HttpResponseForbidden("You are not allowed to mark as paid empty cart")
    cart = Cart.objects.get(id = id)
    cart.paid = 1
    cart.save()

    return HttpResponse("Payment successful for cart I.D " + id)