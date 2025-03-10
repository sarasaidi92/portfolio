from django.shortcuts import render
from django.http import HttpResponse
from.models import Skill, About


def index(request):
    skills = Skill.objects.all()
    abouts = About.objects.all()
    context = {
        'skills': skills,
        'abouts': abouts
    }
    return render(request,template_name='index.html', context=context)