from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def index(request):
    contacts = Contact.objects.all()



    context = {'contacts':contacts}

    return render(request, 'index.html', context=context)