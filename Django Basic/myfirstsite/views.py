from django.shortcuts import render
from employees.models import Employee

def home(request):
        employee = Employee.objects.all()
        context = {
                'employee' : employee,
        }
        # return HttpResponse("Hello World, I'm learning Django!")
        return render(request, "home.html", context)

def about(request):
        return render(request, "about.html")