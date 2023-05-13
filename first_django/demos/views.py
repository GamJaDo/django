from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calculator(reqeust):
    #return HttpResponse("계산기 기능 구현 시작입니다. rr")
    return render(reqeust, 'calculator.html')