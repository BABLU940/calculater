from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

class Simple_calculator(viewsets.ViewSet):

    def addition(self,request):
        print(request)
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        num3 = num1 + num2
        print(num3)
        return Response(num3)

    def subtract(self,request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        num3 = num1 - num2
        print(num3)
        return Response(num3)

    def multiply(self,request):
        num1 = request.data["num1"]
        num2 = request.data['num2']
        num3 = num1 * num2
        print(num3)
        return Response(num3)

    def divide(self,request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        num3 = num1 / num2
        print(num3)
        return Response(num3)
        # num3 = num1 // num2
        # print(num3)
        # return Response(num3)

    def module(self,request):
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        num3 = num1 % num2
        print(num3)
        return Response(num3)



# Create your views here.
