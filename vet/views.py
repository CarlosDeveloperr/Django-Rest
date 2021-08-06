from rest_framework import generics, filters, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
    # Pet serializers
    PetModelSerializer,
    PetListModelSerializer,
    # Pet dates serializers
    PetDateModelSerializer,
    PetDateListModelSerializer,
    PetDatePetRetrieveModelSerializer,
    PetDatePartialUpdateModelSerializer,
)
# Custom permission
from .permissions import OnlyAdminCanCreate
# Models
from .models import PetOwner, Pet, PetDate


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "=last_name"]
    ordering_fields = ["email"]
    permission_classes = [IsAuthenticated, OnlyAdminCanCreate]

    #filter_backends = [DjangoFilterBackend]
    #filterset_fields =  ["first_name","last_name"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class


class PetOwnersDatesListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        filters = {}
        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)


class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "owner__first_name"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer

        return serializer_class

class PetsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer 

class PetDateListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["pet__owner__first_name"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer

        return serializer_class


class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    http_method_names = ["get", "patch", "delete"]
    queryset = PetDate.objects.all()
    serializer_class = PetDatePetRetrieveModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "PATCH":
            serializer_class = PetDatePartialUpdateModelSerializer

        return serializer_class


# ENDPOINTS
# 1. Create date -- DONE
# 2. List all dates -- DONE
# 3. Partial Update date (datetime, type) -- DONE
# 4. Remove date -- DONE
# 5. Retrieve with Pet Information -- DONE
# 6. List dates by pet
# 7. List dates by owner