from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    def create(self, validated_data):
        user=User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eventes
        # fields='__all__'
        exclude=['user',]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        # fields='__all__'
        exclude=['user',]

class CartSerializer(serializers.ModelSerializer):
    events = EventSerializer()
    class Meta:
        model=Cart
        # fields='__all__'
        exclude=['user',]

class AddCartSerializer(serializers.ModelSerializer):
    # events = EventSerializer()
    class Meta:
        model=Cart
        # fields='__all__'
        exclude=['user',]
