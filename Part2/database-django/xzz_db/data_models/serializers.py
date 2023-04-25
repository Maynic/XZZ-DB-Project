from rest_framework import serializers
from .models import xzz_visitor

class VisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = xzz_visitor 
        fields = ("id", "visitor_name", "email", "birth_date", "phone", "address", "city", "state", "zip", "visitor_type")
