from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from inventory.models import Product
from quote.models import Quote
from ..models import Organization, Province, OrganizationProduct
from followup.models import FollowUp


class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = [field.name for field in FollowUp._meta.get_fields()]


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [field.name for field in Quote._meta.get_fields()]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProduct
        fields = [field.name for field in OrganizationProduct._meta.get_fields()]


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = [field.name for field in Province._meta.get_fields()]


class OrganizationSerializer(serializers.ModelSerializer):
    followups = FollowUpSerializer(many=True)
    quotes = QuoteSerializer(many=True)
    province = ProvinceSerializer()
    products = ProductSerializer(many=True)
    registrar = UserSerializer()

    class Meta:
        model = Organization
        fields = [field.name for field in Organization._meta.get_fields()]
