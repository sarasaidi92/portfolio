from django.shortcuts import render
from django.http import HttpResponse
from.models import Skill, About, Basic, Academic


def index(request):
    skills = Skill.objects.all()
    abouts = About.objects.all()
    basics = Basic.objects.all()
    academics = Academic.objects.all()

    context = {
        'skills': skills,
        'abouts': abouts,
        'basics': basics,
        'academics': academics
    }
    return render(request,template_name='index.html', context=context)