from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import employee

# Create your views here.

def get(request):
        return render(request,'login.html')

def gets(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        
        employees=employee.objects.filter(name=name).values('des')
        for emp in employees: 
            emp=emp['des']
            return render(request, "emp.html", {"emp":emp})
    
    return HttpResponse("<h1>Invalid Inputs</h1>")

