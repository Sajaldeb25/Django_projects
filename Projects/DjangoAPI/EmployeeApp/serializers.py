
from rest_framework import serializers

from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields=('__all__')


class EmployeeSerializer(serializers.ModelSerializer):
    Department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employees
        fields=('__all__')


class EmployeeCreateSerializer(EmployeeSerializer):
    Department = serializers.CharField()

    def create(self, validate_data):
        validate_data['Department'] = Departments.objects.get(id=validate_data['Department'])
        print("Validated data--> ",validate_data)
        dept_detail = super().create(validate_data)
        print(dept_detail.Department)
        return dept_detail
    


    



