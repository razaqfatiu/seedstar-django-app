from django.shortcuts import render
from django.http import HttpResponse
from .models import Details

# Create your views here.

def index(request):
    return render(request, "details/welcome.html")
def list(request):
    context = {
        "details": Details.objects.all()
    }
    return render(request, "details/list.html", context)
def add(request):
    return HttpResponse("Add")