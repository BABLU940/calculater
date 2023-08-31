from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

class CalculatorAdvance(viewsets.ViewSet):

    def module(self,request):
        print(request)
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        num3 = num1 % num2
        print(num3)
        return Response(num3)


    def square(self,request):
        print(request)
        num1 = request.data["num1"]
        num2 = num1 * num1
        print(num2)
        return Response(num2)

