from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ss_log/', admin.site.urls),
    path('', include('main.urls')),
]
