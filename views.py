from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
from CRUDOperation.forms import Empforms

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord = EmpModel()
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.salary = request.POST.get('salary')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request,'Employee'+saverecord.name+ 'Is Saved Succesfully...!')
        return render(request,'Insert.html')
    else:
        return render(request,'Insert.html', )

def Editemp(request, id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request,'Edit.html',{"EmpModel":editempobj})

def updateemp(request,id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully...!')
    return render(request,'Edit.html',{"EmpModel":Updateemp})

def Delemp(request,id):
    delemp=EmpModel.objects.get(id=id)
    delemp.delete()
    showdata=EmpModel.objects.all()
    return render(request,"Index.html",{"data":showdata})