from django.shortcuts import render
from api.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class ApiEmp(viewsets.ViewSet):
    def list(self,request):
        emp=Emp.objects.all()
        empl=EmpSerializer(emp,many=True)
        return Response(empl.data)
    
    def create(self,request):
        empsel=EmpSerializer(data=request.data)
        if empsel.is_valid():
            empsel.save()
            return Response({'Success':'Data inserted successfully'})
        else:
            return Response({'Failed':'Something went wrong'})
        
    def retrive(self,request,pk):
        emp=Emp.objects.get(pk=pk)
        empl=EmpSerializer(emp)
        return Response(empl.data)
    
    def update(self,request,pk):
        emp=Emp.objects.get(pk=pk)
        empsel=EmpSerializer(emp,data=request.data)
        if empsel.is_valid():
            empsel.save()
            return Response({'Updated':'Data updated successfully'})
        else:
            return Response({'Failed':'Something went wrong'})
        
    def partial_update(self,request,pk):
        emp=Emp.objects.get(pk=pk)
        empsel=EmpSerializer(emp,data=request.data,partial=True)
        if empsel.is_valid():
            empsel.save()
            return Response({'Updated':'Data partially updated successfully'})
        else:
            return Response({'Failed':'Something went wrong'})
        
    def destroy(self,request,pk):
        emp=Emp.objects.get(pk=pk)
        emp.delete()
        return Response({'Deleted':'Data deleted successfully'})
