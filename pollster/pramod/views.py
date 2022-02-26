
from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse('THIS IS HOME PAGE')
def about(request):
    return render(request,'webss.html')
def search(request):
    aa=open("data.txt",'r')
    vaa1=str(request.POST['DATEE'])
    valuee="not found"
    for line in aa:
        if(vaa1 in line):
            g=line.split()
            valuee=g[0]
    return render(request,'webss.html',{'bpdate':valuee})
def add(request):
    va1=request.POST['bpp']
    va2=request.POST['date']
    aa=open("data.txt",'a')
    aa.write(va1+"  ")
    aa.write(va2+"\n")
    aa.close()   
    return render(request,'webss.html',{"result":"add succesfully"})
# Create your views here.
