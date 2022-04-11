from pyexpat import model
from django.db import models

# Create your models here.

class Departments(models.Model):
    #DepartmentID = models.AutoField(primary_key=True)
    DepartmanetName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Employees(models.Model):
    EmployeeName = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    Email = models.EmailField(max_length=30)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)