from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Converter_system (viewsets.ViewSet):

    def binary_number(self,request):
        decimal_num =request.data["decimal_num"]
        print(request)
        binary_num =""

        while decimal_num > 0:
            remainder = decimal_num % 2
            binary_num = str(remainder) + binary_num
            decimal_num = decimal_num // 2

        return Response(binary_num)

    def decimal_number(self,request):
        print(request)
        binary_num = request.data["binary_num"]
        decimal_num =0
        power = 0
        while(binary_num >0):
            last_digit = binary_num % 10
            decimal_num += last_digit * (2** power)
            binary_num //= 10
            power +=1

        return Response(decimal_num)

