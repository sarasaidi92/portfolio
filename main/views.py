from django.shortcuts import render
from django.http import HttpResponse
from.models import *


def index(request):
    skills = Skill.objects.all()
    abouts = About.objects.all()
    basics = Basic.objects.all()
    academics = Academic.objects.all()
    courses = Course.objects.all()
    researches = Research.objects.all()
    works = Work.objects.all()
    activities = Activity.objects.all()

    context = {
        'skills': skills,
        'abouts': abouts,
        'basics': basics,
        'academics': academics,
        'courses': courses,
        'researches': researches,
        'works': works,
        'activities': activities

    }
    return render(request,template_name='index.html', context=context)