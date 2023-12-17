from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from .models import Person

# Create your views here.
def index(request):
    return render(request,'users/index.html',{'users':Person.objects.all()})

def view_user(request,id):
    user = Person.objects.get(pk=id)
    return HttpResponseRedirect(reverse(index))
