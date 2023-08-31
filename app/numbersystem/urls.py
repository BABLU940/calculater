from django.urls import path
from .views import Converter_system

urlpatterns=[
    path('p/binary_number',Converter_system.as_view({'get':'binary_number'})),
    path('p/decimal_number',Converter_system.as_view({'get':'decimal_number'})),
]