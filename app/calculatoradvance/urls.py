from django.urls import path
from .views import AdvanceCalculator

urlpatterns=[
    path('p/even',AdvanceCalculator.as_view({'get':'even'})),
    path('p/odd',AdvanceCalculator.as_view({'get':'odd'})),
]