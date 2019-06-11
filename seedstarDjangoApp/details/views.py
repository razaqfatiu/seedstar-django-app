from django.shortcuts import render
from django.http import HttpResponse
from .models import Details as details
from details.forms import Details
# Create your views here.

def index(request):
    return render(request, "details/welcome.html")
def list(request):
    context = {
        "details": details.objects.all()
    }
    return render(request, "details/list.html", context)
class add():
    template_name = "details/add.html"
    def get(self, request):
        form = Details()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = Details(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['name', 'email']

        return render(request, self.template_name, {'form': form})