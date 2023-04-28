from rest_framework import serializers
from .models import xzz_visitor

class VisitorSerializer(serializers.ModelSerializer):

    # visitor_type_full = serializers.CharField(source='get_visitor_type_display')

    class Meta:
        model = xzz_visitor 
        # fields = ("id", "visitor_name", "email", "birth_date", "phone", "address", "city", "state", "zip", "visitor_type",visitor_type_full)
        fields = '__all__'
