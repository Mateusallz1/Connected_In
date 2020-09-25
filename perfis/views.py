from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def exibir_perfil(request, perfil_id): 
    perfil = Perfil()
    perfil = Perfil.objects.get(id = perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil})
    
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index') #Redirect apenas retorna para a página index.

def get_perfil_logado(request):
    return Perfil.objects.get(id = 1)
# Create your views here.
