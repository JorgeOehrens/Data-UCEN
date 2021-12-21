from django.shortcuts import render
from .models import Detalle 
# Create your views here.

def index(request):

    detalle = Detalle.objects.all()
    context = {
        'detalle': detalle
    }




    if request.method =='GET':


        return render(request, 'index/index.html', context)