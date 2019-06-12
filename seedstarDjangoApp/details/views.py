from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Details
# from details.forms import Details
# Create your views here.

def index(request):
    return render(request, "details/welcome.html")
def list(request):
    context = {
        "details": Details.objects.all()
    }
    return render(request, "details/list.html", context)

def add(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            form = Details()
            form.name = request.POST.get('name')
            form.email = request.POST.get('email')
            form.save()
            return HttpResponseRedirect("list")
            
            
    else:
        form = Details()
        # return render(request, self.template_name, {'form': form})
        return render(request, "details/add.html")