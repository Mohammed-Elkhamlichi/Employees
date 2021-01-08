from django.urls import path
from .views import add_employee

# app name.
app_name = 'employee'


# urlpatterns.
urlpatterns = [
    path('add/', add_employee, name='add_employee'),
]