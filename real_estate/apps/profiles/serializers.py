from dataclasses import field
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    firstname = serializers.CharField(source='user.firstname')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Profile
        fields =[
            'id', 
            'username',
            'email',
            'firstname',
            'last_name',
            'full_name', 
            'gender', 
            'phone_number',
            'profile_photo',
            'country',
            'about_me', 
            'city',
            'is_buyer',
            'is_seller',
            'is_agent',
            'ratings',
            'numb_reviews',
            'reviews',
            'license',
        ]
    def get_full_name(self,obj):
        firstname =obj.user.firstname.title()
        last_name = obj.user.last_name.title()
        return f"{firstname} {last_name}"
    
    def get_reviews(self, obj):
        reviews = obj.user.agent_review.all()
        serializers = RatingSerializer(reviews, many=True)
        return serializers.data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True
        return representation
    
class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    
    class Meta:
        model = Profile
        fields =[
            'phone_number',
            'profile_photo',
            'about_me',
            'license', 
            'gender',
            'country',
            'city',
            'is_buyer',
            'is_seller',
            'is_agent'    
        ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True
        return representation