from django.shortcuts import render
from django.shortcuts import render, redirect  
from crud.forms import CrudForm  
from crud.models import Crud  

def api(request):  
    if request.method == "POST":  
        form = CrudForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CrudForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    cruds = Crud.objects.all()  
    return render(request,"show.html",{'cruds':cruds})  

def edit(request, id):  
    crud = Crud.objects.get(id=id)  
    return render(request,'edit.html', {'crud':crud})  

def update(request, id):  
    crud = Crud.objects.get(id=id)  
    form = CrudForm(request.POST, instance = crud)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'crud': crud})  

def destroy(request, id):  
    crud = Crud.objects.get(id=id)  
    crud.delete()  
    return redirect("/show")