from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def greeting(request):
    s="<h1>GREETING FROM ME!!</h1>"
    return HttpResponse(s)

def contact(request):
    s="<h2>Contact form</h2>"
    s+="<p>NAME:Monty singh</p>"
    s+="<p>Contact:9080765512</p>"
    s+="<p>www.easy.com</p>"
    return HttpResponse(s)

def about(request):
    s="THIS IS MADE BY JAGMEET SINGH"
    #a=[10,20,30]
    #x=12
    #return render(request,'testapp/about.html',{'s':s,'a':a,'x':x})
    return render(request,'testapp/about.html',{'s':s})
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    return render(request,'testapp/employee.html',data)
