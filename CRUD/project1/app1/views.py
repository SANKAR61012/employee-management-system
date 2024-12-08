from django.shortcuts import render,redirect
from app1.models import Datas

# Create your views here.
def home(request):  #127.0.0.1:8000
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:    
        return render(request,"home.html")
def addData(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        salary=request.POST['salary']
        mail=request.POST['mail']

        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Salary=salary
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect('home') 
    return render(request,"home.html")
def updateData(request,id):#127.0.0.8000:updateData/18
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        salary=request.POST['salary']
        mail=request.POST['mail']

        
        mydata.Name=name
        mydata.Age=age  
        mydata.Address=address
        mydata.Contact=contact
        mydata.Salary=salary
        mydata.Mail=mail
        mydata.save()
        return redirect('home')
    return render(request,'update.html',{'data':mydata})        
def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')
