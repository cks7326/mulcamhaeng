#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def home(reqData):
    return HttpResponse("안녕~ : HTTP 출력 기능 사용")