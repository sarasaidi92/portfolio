from django.shortcuts import render
from django.http import HttpResponse
from.models import Skill


def index(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request,template_name='index.html', context=context)