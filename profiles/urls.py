from django.urls import path
from .views import test

# app name.
app_name = 'profiles'


# url patterns.

urlpatterns = [
    path('test/', test, name='test'),
]