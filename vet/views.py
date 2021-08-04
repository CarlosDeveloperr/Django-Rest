from rest_framework import generics

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
    PetsListModelSerializer,
    DatesListModelSerializer
)

# Models
from .models import PetOwner, Pet,PetDate


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class


class PetsListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetsListModelSerializer

    def get_queryset(self):

        name_filter = self.request.GET.get("name")
        filters = {}
        if name_filter:
            filters["name__icontains"] = name_filter

        return self.queryset.filter(**filters)



class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer


class PetsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = DatesListModelSerializer

class DatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesListModelSerializer

class DatesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesListModelSerializer