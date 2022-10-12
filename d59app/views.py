from django.shortcuts import render,HttpResponseRedirect
from .forms import Registartion
from .models import Add
# add and show views here ..
def add_show(request):
    if request.method == 'POST':
        fm=Registartion(request.POST)
        if fm.is_valid():
          name=fm.cleaned_data['name']
          email=fm.cleaned_data['email']
          password=fm.cleaned_data['password']
          reg=Add(name=name,email=email,password=password)        
          reg.save()  
          fm=Registartion()
    else:
        fm=Registartion()
    student=Add.objects.all()
    return render(request,'app/addandshow.html',{'form':fm,'student':student})

# This function will update
def update_data(request,id):
    if request.method=='POST':
        pi=Add.objects.get(pk=id)
        fm=Registartion(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Add.objects.get(pk=id)
        fm=Registartion(instance=pi)
    return render(request,'app/update.html',{'id':id,'form':fm})

# This function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi=Add.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

        