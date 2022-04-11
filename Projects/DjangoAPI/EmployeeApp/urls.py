from django.urls import path
from EmployeeApp import views

urlpatterns=[
    path('department/', views.DepartmentView.as_view(), name='departments'),
    #path('department/<int:pk>/', views.DepartmentView.as_view(), name='departmentupdate'),
    path('employee/', views.EmployeeView.as_view(), name='Employyes' )
]