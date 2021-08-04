  
from django.db import models
from rest_framework import serializers
from .models import PetOwner,Pet,PetDate


class PetOwnersListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]


class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "address", "phone", "email"]


class PetsListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id","name", "type", "owner"]

class DatesListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["datetime", "type", "pet"]

     