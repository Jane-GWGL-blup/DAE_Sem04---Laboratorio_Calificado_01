from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    #ex: /registro/
    path('', views.index, name='index'),
    #ex: /registro/5/
    path('<int:region_id>/', views.resultado, name='resultado'),
    # ex: /registro/detalles/5/
    path('detalles/<int:candidato_id>/', views.detalles, name='detalles'),
]