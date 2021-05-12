from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse('This Is Home Page')
def about(request):
    return HttpResponse('This Is About Page')
def help(request):
    return HttpResponse('This Is Help Page')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse('This Is Contact Page')