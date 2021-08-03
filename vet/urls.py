from django.urls import path

#views
from .views import (
# PetOwnersListCreateAPIView,
# PetsListCreateAPIView,
# PetOwnerRetrieveUpdateDestroyAPIView,
# PetRetrieveUpdateDestroyAPIView,
#generics
PetOwnersListAPIView,
PetOwnerRetrieveAPIView,
##PETS
PetsListAPIView,
PetsRetrieveAPIView,
) 
                   
urlpatterns = [
        ##Genericas
    path("owners/", PetOwnersListAPIView.as_view(), name="owners_list-create"),
    path("pets/", PetsListAPIView.as_view(), name="pets_list"),
    path("pets/<int:pk>", PetsRetrieveAPIView.as_view(), name="pets_retrieve"),
    path("owners/<int:pk>", PetOwnerRetrieveAPIView.as_view(), name="owners_retrieve"),
    ##################################################################
    # path("owners/",PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve-update-destroy"),
    # path("pets/",PetsListCreateAPIView.as_view(), name="pet_list"),
    # path("pets/<int:pk>",PetRetrieveUpdateDestroyAPIView.as_view(), name="pet_retrieve-update-destroy"),
]