
from home.models import Setting
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from  home.models import *
# Create your views here.
def index(request):

    setting = Setting.objects.get(pk = 1)
    page = "home"
    context = {'setting': setting, 'page': page}
    return render(request, 'home/index.html', context)

def aboutUs(request):   
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'home/about.html', context)

def contact(request):
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting': setting, 'form': form}
    return render(request, 'home/contact.html', context)
