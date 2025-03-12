from django.contrib import admin
from.models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')

admin.site.register(Contact, ContactAdmin)


