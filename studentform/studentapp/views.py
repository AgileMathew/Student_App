from django.shortcuts import render
from studentapp.models import Data
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def details(request):
    
    if request.method == 'POST':
        
        data = request.POST
        
        d= Data()
        d.name = data['name']
        d.rollno = data['rollno']
        d.age = data['age']
        
        d.save()

        return HttpResponseRedirect('/studentform/show/')
    return render(request, "studentapp/details.html", {})

def show(request):
    datas = Data.objects.all().values()
    print datas
    return render(request, "studentapp/show.html", {'data': datas})