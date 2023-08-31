from django.urls import path
from .views import Simple_calculator

urlpatterns=[
    path('p/addition',Simple_calculator.as_view({'get':'addition'})),
    path('p/subtract',Simple_calculator.as_view({'get':'subtract'})),
    path('p/multiply',Simple_calculator.as_view({'get':'multiply'})),
    path('p/divide',Simple_calculator.as_view({'get':'divide'})),
    path('p/module',Simple_calculator.as_view({'get':'module'})),
]