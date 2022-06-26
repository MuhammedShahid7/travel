from django.shortcuts import render

# Create your views here.
from .models import Place, Heroes


def demo(request):
    obj = Place.objects.all()
    obj1 = Heroes.objects.all()
    return render(request, "index.html", {'result': obj,'results': obj1})
