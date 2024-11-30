from django.urls import path
from .views import v_index, v_providers, v_customers, v_pet

urlpatterns = [
    path("", v_index, name="index"),
    path("providers", v_providers, name="providers"),
    path("customers", v_customers, name="customers"),
    path("pet", v_pet, name="pet"),
]
