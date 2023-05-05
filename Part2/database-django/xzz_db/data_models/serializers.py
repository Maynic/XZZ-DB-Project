from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_visitor 
        fields = ("id", "visitor_name", "email", "birth_date", "phone", "address", "city", "state", "zip", "visitor_type")


class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_ticket_search
        fields = ("id", "radio", "ticket_date", "ticket_c", "ticket_a", "ticket_s",
                  "show_select", "show_date", "show_c", "show_a", "show_s", "store_category",
                  "park_place", "park_in_date", "park_in", "park_out_date", "park_out")

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_user_login
        fields = ("id", "fname", "lname", "email", "password")