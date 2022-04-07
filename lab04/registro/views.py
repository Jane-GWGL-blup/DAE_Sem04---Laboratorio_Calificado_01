from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Region, Candidato
#vista principal
def index(request):
    region_list = Region.objects.order_by('id')
    context = {'region_list': region_list}
    return render(request, 'registro/index.html', context)
#vista resultado
def resultado(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'registro/resultado.html',{'region': region})
#Detalle de candidatos
def detalles(request, candidato_id):
    candidato = get_object_or_404(Candidato, pk=candidato_id)
    return render(request, 'registro/detalles.html',{'candidato': candidato})
