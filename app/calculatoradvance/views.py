from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

class AdvanceCalculator(viewsets.ViewSet):

    def even(self,request):
        print(request)
        num1 = request.data["num1"]
        if(num1 % 2 == 0):
            return Response("num1 is even number")
        else:
            return Response("num1 is odd number")
        return Response()

    def odd(self,request):
        print(request)
        # request is a object and data is property of request []
        # num2 = request.data["num2"]
        num2 = request.data.get('num2')
        if(num2 % 2 != 0):
            return Response(True)
        return Response(False)


# Create your views here.
