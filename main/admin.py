from django.contrib import admin
from.models import Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']
    list_display_links = ['title']
    list_editable = ['percent']

admin.site.register(Skill, SkillAdmin)


