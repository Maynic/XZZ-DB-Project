from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):
    visitor_type_full = serializers.CharField(required=False, source='get_visitor_type_display')
    class Meta:
        model = xzz_visitor 
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_ticket_search
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_user_login
        fields = '__all__'
        # fields = ("id", "visitor_name", "email", "birth_date", "phone", "address", "city", "state", "zip", "visitor_type",visitor_type_full)
        fields = '__all__'


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_attraction
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_order 
        fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_parking
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_payment
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_show 
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_store 
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_ticket 
        fields = '__all__'

class AttractionVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_attr_visi 
        fields = '__all__'

class ShowOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_orde_show 
        fields = '__all__'

class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = xzz_orde_stor 
        fields = '__all__'
