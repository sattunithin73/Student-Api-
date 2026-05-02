from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','DELETE'])
def students(request):
    model_instance = StudentModel.objects.all()
    #read operation
    if request.method == 'GET':
        ser_data = StudentSerializer(model_instance,many=True)
        py_data = ser_data.data
        return Response(py_data)
        #whenever we are using api_view decorator we will returing response through Response class
        #when we are using Response class we can directly pass the python data internally it will get converted json
    
    #CREATE OPERATION
    if request.method == 'POST':
        # req_data = request.body
        # print(req_data)#json byte data
        # stream_data = io.BytesIO(req_data)
        # py_data = JSONParser().parse(stream_data)
        py_data = request.data
        print(py_data)

        #deserialization
        de_ser = StudentSerializer(data = py_data)

        if de_ser.is_valid():
            de_ser.save()
            # return Response({'msg':'data created in backend database'})
            return Response(status=status.HTTP_201_CREATED)
        
    #delete operation
    if request.method == 'DELETE':
        model_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def student(request,id):
    try:
        model_instance = StudentModel.objects.get(id=id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        ser_py = StudentSerializer(model_instance)
        py_data = ser_py.data
        print(py_data)
        return Response(py_data) 
    
    if request.method == 'PUT':
        py_data = request.data
        print(py_data)
        de_ser = StudentSerializer(model_instance,data=py_data)
        if de_ser.is_valid():
            de_ser.save()
            return Response(status=status.HTTP_202_ACCEPTED)

    if request.method == 'DELETE':
        model_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    