from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class Dash(View):
    def get(self, request, *args, **kwargs):
        context = {}
        leituras = Leitura.objects.all()
        context['leituras'] = leituras
        return render(request, 'dashboard.html', context)
    def post(self, request, *args, **kwargs):
        pass