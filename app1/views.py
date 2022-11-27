from django.shortcuts import render,redirect
from.forms import Addlandform,Addplotform

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