  
from django.db import models
from rest_framework import serializers
from .models import PetOwner, Pet, PetDate


class PetOwnersListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]


class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "address", "phone", "email"]


class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "owner"]


class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "owner"]


class PetDateListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "pet"]


class PetDateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"]


class PetDatePetRetrieveModelSerializer(serializers.ModelSerializer):

    pet = PetModelSerializer()

    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"]


class PetDatePartialUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["datetime", "type"]

     