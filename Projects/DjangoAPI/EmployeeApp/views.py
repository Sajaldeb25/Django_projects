from django.core.exceptions import *


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from EmployeeApp.models import Employees, Departments
from EmployeeApp.serializers import EmployeeSerializer, DepartmentSerializer
from EmployeeApp.serializers import EmployeeCreateSerializer

class DepartmentView(APIView):
    def get(self, request):
        departments = Departments.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.data) #.................................................--------------- printrd for check
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        deptartment_id = request.data['DepartmentID'] 
        #print(deptartment_id)
        id = Departments.objects.get(DepartmentID = deptartment_id)
        #print(id)
        serializer = DepartmentSerializer(id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        deptartment_id = request.data['DepartmentID'] 
        id = Departments.objects.get(DepartmentID = deptartment_id)
        id.delete()
        res = {'msg': 'Deleted Sucessfully.'}
        return Response(res)


class EmployeeView(APIView):
    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EmployeeCreateSerializer(data=request.data)

        try:
            if Departments.objects.get(id = request.data['Department']):
                if serializer.is_valid():
                    serializer.save()
                    details_serializer= EmployeeSerializer(instance = serializer.instance) ## for accessing full employee info
                    print(details_serializer.data)
                    return Response(details_serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Departments.DoesNotExist:
            res = {'msg': 'Dept does not exist.'}
            return Response(res)

    def put(self, request, format=None):
        employee_id = request.data['id'] 
        #print(employee_id)
        id = Employees.objects.get(id = employee_id)
        #print(id)
        serializer = EmployeeSerializer(id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        employee_id = request.data['id']
        id = Employees.objects.get(id = employee_id)
        id.delete()
        res = {'msg': 'Employee deleted Sucessfully.'}
        return Response(res)



