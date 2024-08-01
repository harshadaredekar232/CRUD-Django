from django.shortcuts import render,redirect,HttpResponse
from .models import Staff,Student
# Create your views here.

def display(req):
    m = Student.objects.all()
    print(m)
    st = Staff.objects.all()
    print(st)
    return render(req, "index.html",{'student':m, 'staff': st})

def create(req):
    if req.method == "GET":
        return render(req, 'create.html')
    else:
        id = req.POST["id"]
        name = req.POST.get("name")
        mail = req.POST["mail"]
        mob = req.POST["mobile"]
        dob = req.POST["dob"]
        print(id,name,mail,mob,dob)
        #insert into model # fieldname = python_variable
        Student.objects.create(id=id,name=name,email=mail,mobile=mob,dob=dob)
        #return render(req, 'index.html') 
        return redirect("/")
    
def create_Staff(req):
    if req.method == "GET":
        return render(req, 'create.html')
    else:
        id = req.POST["id"]
        name = req.POST.get("name")
        mail = req.POST["mail"]
        mob = req.POST["mobile"]
        dob = req.POST["dob"]
        print(id,name,mail,mob,dob)
        #insert into model # fieldname = python_variable
        Staff.objects.create(id=id,name=name,email=mail,mobile=mob,dob=dob)
        #return render(req, 'index.html') 
        return redirect("/")
    
def edit(req,sid):
    m = Student.objects.get(id=sid)
    if req.method == 'GET':
        return render(req, "update.html", {"data":m})
    else:
        id = req.POST["id"]
        name = req.POST["name"]
        mail = req.POST["mail"]
        mob = req.POST["mobile"]
        dob = req.POST["dob"]
        gender = req.POST["gender"]
        print(id,name,mail,mob,dob)
        #insert into model # fieldname = python_variable
        data = Student.objects.filter(id=id)
        data.update(id=id,name=name,email=mail,mobile=mob,dob=dob,gender=gender)
        #return render(req, 'index.html') 
        return redirect("/")

def delete(req,sid):
    m = Student.objects.get(id = sid)
    print(m)
    m.delete()
    return redirect("/")

def search_male(req):
    data = Student.objects.filter(gender__iexact = "male")
    return render(req, "index.html",{"student":data})

def search_female(req):
    data = Student.objects.filter(gender__iexact = "female")
    return render(req, "index.html",{"student":data})