from django.urls import path
from .views import add_employee, remove_employee, update_employee

# app name.
app_name = 'employee'


# urlpatterns.
urlpatterns = [
    path('add/', add_employee, name='add_employee'),
    path('<int:pk>/remove', remove_employee, name='remove_employee'),
    path('<int:pk>/update/', update_employee, name='update_employee'),
]