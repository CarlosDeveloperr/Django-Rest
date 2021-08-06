from django.urls import path
from rest_framework.authtoken import views as authtoken_views
# Views
from .views import (
    # Pet owners
    PetOwnersListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
    PetOwnersDatesListCreateAPIView,
    # Pet
    PetListCreateAPIView,
    PetsRetrieveUpdateDestroyAPIView,
    # Pet dates
    PetDateListCreateAPIView,
    PetDateRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
     # Login
    path("token-auth/", authtoken_views.obtain_auth_token, name="token_auth"),
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path(
        "owners/<int:pk>",
        PetOwnersRetrieveUpdateDestroyAPIView.as_view(),
        name="owners_retrieve-update-destroy",
    ),
    path(
        "owners/<int:pk>/dates",
        PetOwnersDatesListCreateAPIView.as_view(),
        name="owners_dates_list",
    ),
    # Pets
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>",PetsRetrieveUpdateDestroyAPIView.as_view(),name="pets_retrieve-update-destroy"),
    # Pet dates
    path("dates/", PetDateListCreateAPIView.as_view(), name="dates_list-create"),
    path(
        "dates/<int:pk>",
        PetDateRetrieveUpdateDestroyAPIView.as_view(),
        name="dates_retrieve-update-destroy",
    ),
]