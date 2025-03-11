from django.contrib import admin
from.models import Skill, About, Basic, Academic, Course

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']
    list_display_links = ['title']
    list_editable = ['percent']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


class BasicAdmin(admin.ModelAdmin):
    list_display = ['name','title']
    list_display_links = ['title']

class AcademicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


admin.site.register(Skill, SkillAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Basic, BasicAdmin)
admin.site.register(Academic, AcademicAdmin)
admin.site.register(Course, CourseAdmin)



