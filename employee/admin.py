from django.contrib import admin
from .models import Employee

# Register your models here.


# register the employee model in the admin page.
admin.site.register(Employee)