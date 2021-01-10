from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employee
# Create your views here.




def add_employee(request):
    employees = Employee.objects.all().order_by('first_name')
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    context = {
        'form': form,
        'employees': employees,
        'dev': 'Mohammed Elkhamlichi'
    }
    return render(request, 'add_employee.html', context)




def remove_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'employee has been deleted')
        return redirect('employee:add_employee')


    context = {"employee": employee}
    return render(request, 'remove_employee.html', context)




def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been updated')
            return redirect('employee:add_employee')
            
    context = {"form":form}

    return render(request, 'update_employee.html', context)
