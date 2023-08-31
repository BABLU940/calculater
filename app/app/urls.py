from django.urls import path
from .views import CalculatorAdvance

urlpatterns = [
    path('p/module',CalculatorAdvance.as_view({'post': 'module'})),
    path('p/square',CalculatorAdvance.as_view({'get':'square'})),

]