from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# Create your views here.

def add_employee(request):
    form = EmployeeForm()
    context = {
        'form': form,
        'dev': 'Mohammed Elkhamlichi'
    }
    return render(request, 'add_employee.html', context)
