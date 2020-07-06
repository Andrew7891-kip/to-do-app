from django.shortcuts import render,redirect
from .models import Written
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
# from .forms import Add

def index(request):
    written=Written.objects.all()
    return render(request,'index.html',{'written':written})


def addTodoView(request):
    
    new_item = Written (content=request.POST.get('content'))
    new_item.save()
    return redirect('/')

def deleteTodo(request,pk):
    c=Written.objects.get(pk=pk)
    c.delete()
    return redirect('/')







