from django.shortcuts import render
from .models import Detalle , Exportador , Pais
# Create your views here.

def index(request):

    detalle = Detalle.objects.all()
    context = {
        'detalle': detalle
    }




    if request.method =='GET':


        return render(request, 'index/index.html', context)
    
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        detalle_table = Detalle.objects.all().order_by('-fecha')

        #filterdates
        if start_date and end_date:
            detalle_table = detalle_table.filter(fecha__gte=start_date, fecha__lte=end_date)
        
        context = {
            'detalle':detalle_table,
        }

        return render(request, 'index/index.html', context)

def tipo_trasporte(request):

    detalle = Detalle.objects.all()
    context = {
        'detalle': detalle,
    }




    if request.method =='GET':
        
        return render(request, 'index/tipo_transporte.html', context)
    
    if request.method == 'POST':
        filtrado = request.POST['filtrado']
        
        detalle_table = Detalle.objects.filter(tipo_transporte=filtrado)
        pais = Pais.objects.all()

        
        detalle_table=detalle_table.order_by('-fecha')
        
        context = {
            'detalle':detalle_table,

        }
        return render(request, 'index/tipo_transporte.html', context)


def pais(request):

    detalle = Exportador.objects.all()
    pais = Pais.objects.all()

    context = {
        'detalle': detalle,
        'pais': pais,

    }




    if request.method =='GET':


        return render(request, 'index/pais.html', context)
    
    if request.method == 'POST':
        filtrado = request.POST['filtrado']


        detalle_table = Exportador.objects.filter(pais_id=filtrado)
        
        pais = Pais.objects.all()
    
    
        
        
        context = {
            'detalle':detalle_table,
            'pais': pais,

            
        }
        return render(request, 'index/pais.html', context)

def cantidad(request):

    detalle = Detalle.objects.all()
    context = {
        'detalle': detalle,
    }




    if request.method =='GET':
        
        return render(request, 'index/cantidad.html', context)
    
    if request.method == 'POST':
        filtrado = request.POST['filtrado']
        detalle_table = Detalle.objects.all()

        # detalle_table = Detalle.objects.filter(cantidad=filtrado)

        detalle_table = detalle_table.filter(cantidad__gte=filtrado)
        detalle_table=detalle_table.order_by('-cantidad')
        
        context = {
            'detalle':detalle_table,

        }
        return render(request, 'index/cantidad.html', context)


def descripcion(request):

    detalle = Detalle.objects.all()
    context = {
        'detalle': detalle,
    }




    if request.method =='GET':
        
        return render(request, 'index/cantidad.html', context)
    
    if request.method == 'POST':
        filtrado = request.POST['filtrado']
        detalle_table = Detalle.objects.all()

        # detalle_table = Detalle.objects.filter(cantidad=filtrado)

        detalle_table = detalle_table.filter(cantidad__gte=filtrado)
        detalle_table=detalle_table.order_by('-cantidad')
        
        context = {
            'detalle':detalle_table,

        }
        return render(request, 'index/cantidad.html', context)
