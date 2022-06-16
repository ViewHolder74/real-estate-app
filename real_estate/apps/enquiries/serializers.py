from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = "__all__"
        
