from django.forms import fields  
from .models import Department ,User 
from django import forms  
  
class DepartmentForm(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = Department  
        # It includes all the fields of model  
        fields = '__all__'  
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'