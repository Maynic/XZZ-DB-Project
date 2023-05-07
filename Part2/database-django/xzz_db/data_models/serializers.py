from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):
    visitor_type_full = serializers.CharField(required=False, source='get_visitor_type_display')
    class Meta:
        model = xzz_visitor 
        fields = '__all__'


# class SearchSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = xzz_search
#         fields = '__all__'
#
    # def valid(self):
    #     if self.validated_data['radio'] == "form1" and (self.validated_data['ticket_date'] == "") or \
    #             (self.validated_data['ticket_date'] != "" and
    #                                                     (self.validated_data['ticket_c'] == "" and
    #                                                     self.validated_data['ticket_a'] == "" and
    #                                                     self.validated_data['ticket_s'] == "")
    #     ):
    #         return False
    #     elif self.validated_data['radio'] == "form2" and (self.validated_data['show_date'] == "") or \
    #             (self.validated_data['show_date'] != "" and
    #                                                     (self.validated_data['show_c'] == "" and
    #                                                     self.validated_data['show_a'] == "" and
    #                                                     self.validated_data['show_s'] == "")
    #     ):
    #         return False
    #     elif self.validated_data['radio'] == "form3" and (self.validated_data['store_category'] == "Select choice"):
    #         return False
    #     elif self.validated_data['radio'] == "form4" and (self.validated_data['park_place'] == "Select choice"):
    #         return False
    #     return True

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_user_login
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
