from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print("ddd")
    # return HttpResponse("hellp")
    return render(request,'index.html')