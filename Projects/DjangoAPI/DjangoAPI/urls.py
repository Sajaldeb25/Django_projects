from django.contrib import admin
from django.urls import path, include

from EmployeeApp import views

urlpatterns = [
    path('', include('EmployeeApp.urls')),
    path('admin/', admin.site.urls),
]
