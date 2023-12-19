from django.http import HttpResponse
import datetime
from django.shortcuts import *

def home(request):
    isActive = True
    if request.method == "POST":
        check_name = request.POST.get("check_name")
        print(check_name)
        if check_name is None:
            isActive = False
        else:
            isActive = True
    
    date_now = datetime.datetime.now()
    name= "learn_python_with_buluu"
    list_of_progs = [
        "WAP to get prime no",
        "WAP to get even or odd",
        "WAP to print 1-100"
    ]
    student = {
        "name": "foty",
        "age": 18,
        "hobby": "sleep all day"
    }
    
    
    data = {
        "date": date_now,
        "isactive": isActive,
        "names": name,
        "list_of_progs": list_of_progs,
        "student_data": student
    }
    return render(request,"index.html", data )







def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{} )



def services(request):
    # return HttpResponse("<h1>This is the services page</h1>")
        return render(request,"services.html",{} )
