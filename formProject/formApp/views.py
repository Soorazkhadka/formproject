from django.shortcuts import render
from . import forms

# Create your views here.
reg_form=forms.studentRegistration()
def reg(request):
    return render(request,'formapp/index.html',{'form':reg_form})
