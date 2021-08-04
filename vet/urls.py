from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListCreateAPIView,
    PetsListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
    PetsRetrieveUpdateDestroyAPIView,
    #Dates
    DatesListCreateAPIView,
    DatesRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path("pets/", PetsListCreateAPIView.as_view(), name="pets_list-create"),
    path("owners/<int:pk>",PetOwnersRetrieveUpdateDestroyAPIView.as_view(),name="owners_retrieve-update-destroy"),
    path("pets/<int:pk>",PetsRetrieveUpdateDestroyAPIView.as_view(),name="pets_retrieve-update-destroy"),
    path("dates/", DatesListCreateAPIView.as_view(), name="dates_list-create"),
    path("dates/<int:pk>",DatesRetrieveUpdateDestroyAPIView.as_view(),name="dates_retrieve-update-destroy"),
]


