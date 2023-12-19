from .models import emps
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *



# Create your views here.

def employee_home(request):

    emp_s = emps.objects.all()
    return render(request, "employee/index.html", {
        "emp_s": emp_s
    } )



def add_emp(request):
    if request.method == "POST":

        # fetch data
        emp_name = request.POST.get( "emp_name" )
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        #create model object and create data
        e = emps()

        e.name = emp_name
        e.id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
    
        # save object
        e.save()

        # prepare msg




        return redirect("/employee/home/")
    return render(request, "employee/add_emp.html", {})



def delete_employee(request, emp_id):
    emp = emps.objects.get(pk=emp_id)
    emp.delete()
    # print("Deleted the id ", emp_id )
    return redirect("/employee/home/")


def update_employee(request, emp_id):
    emp = emps.objects.get(pk=emp_id)
    return render(request, "employee/update_employee.html", {
        "emp": emp
    } )
    
def do_update_employee(request, emp_id):
    if request.method == "POST":
        # fetch data
        emp_name = request.POST.get( "emp_name" )
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        e = emps.objects.get(pk=emp_id)
        e.name = emp_name
        e.id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        e.save()

    return redirect("/employee/home/")  




def feedback(request):
    if request.method == "POST":
        form = feedback_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "employee/feedback.html",{
            "feed_form": form
            })
            
    else:
        form = feedback_Form()
        return render(request, "employee/feedback.html",{
            "feed_form": form
            })