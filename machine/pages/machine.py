
from django.shortcuts import render

# Create your views here.

class MachinePage():

    def index(request):
        return render(request,'index.html')