from .models import destination
from django.shortcuts import render,HttpResponse
def home(request):
    d1=destination("mumbai","city thaat never sleeps",500)
    return render(request,'index.html',{'dest':d1})
# Create your views here.
