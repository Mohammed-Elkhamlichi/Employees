from django import forms
from django.forms import widgets
from .models import Employee

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'btn btn-success border border-light text-left',
                # 'id':'first_name'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'btn btn-success border border-light text-left'
            }
        )
    )
    
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')