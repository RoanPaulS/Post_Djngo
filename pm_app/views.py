from django.shortcuts import render
from django.http import HttpResponse

def perform_page(request):
    return render(request,'perform.html',{})

def result_page(request):
    value1 = int(request.POST["number1"])
    value2 = int(request.POST["number2"])
    result_val = value1 + value2
    return render(request,"result.html",{'result':result_val})
