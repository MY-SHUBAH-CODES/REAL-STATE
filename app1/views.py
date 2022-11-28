from django.shortcuts import render,redirect
from.forms import Addlandform,Addplotform
from.models import Addland,Addplot

# Create your views here.
def home(request):
    return render(request,'base.html',)


def addland(request):
    if request.method=='POST':
        form=Addlandform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('.')
    else:
        return render(request,'add_land.html',{'form':Addlandform})


def addplot(request):
    if request.method=='POST':
        form=Addplotform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('.')
    else:
        return render(request,'add_plot.html',{'form':Addplotform})


def landdetails(request,pk):
    data=Addland.objects.get(id=pk)
    return render(request,'landdetails.html',{'data':data})

def allland(requst):
    data=Addland.objects.all()
    for i in data:
        print(i.id)
    return render(requst,'all_lands.html',{'data':data})