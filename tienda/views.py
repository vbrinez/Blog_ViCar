from urllib import request
from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.

def verproductos(request):
    return render(request, "productos.html", {'nombre':'Victor','nombre_completo':'Victor Briñez','id_usuario':'1'})