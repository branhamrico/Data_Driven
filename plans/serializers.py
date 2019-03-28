from django.contrib.auth.models import User, Group
from .models import Cart, CartItem, Provider, Term, Plan
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('__all__')

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'paid', 'client', 'cart_items')

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('__all__')

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('__all__')

class PlanSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name')

    class Meta:
        model = Plan
        fields = ('id', 'name', 'description', 'cost', 'provider', 'provider_name')