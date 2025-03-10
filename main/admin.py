from django.contrib import admin
from.models import Skill, About, Basic

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']
    list_display_links = ['title']
    list_editable = ['percent']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    list_display_links = ['title']
    list_editable = ['text']

class BasicAdmin(admin.ModelAdmin):
    list_display = ['name','title']
    list_display_links = ['title']


admin.site.register(Skill, SkillAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Basic, BasicAdmin)



