from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # use seu form correto

def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso. Agora faça login.')
            return redirect('login')  # nome da url do login
    else:
        form = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pag_inicial')  # nome da url da página inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

@login_required
def pag_inicial(request):
    return render(request, 'pag_inicial.html')

def fabrica2(request):
    return render(request, 'fabrica_2/fabrica2.html')

def prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/prensas_fabrica2.html')

def omera1_prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera1_prensas_fabrica2.html')

def omera2_prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera2_prensas_fabrica2.html')

def omera3_prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera3_prensas_fabrica2.html')

def omera4_prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera4_prensas_fabrica2.html')

def perfiladora_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2//perfiladora_fabrica2.html')

def cosma_perfiladoras_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/cosma_perfiladoras_fabrica2.html')

def fagorGabinete_perfiladoras_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/fagorGabinete_perfiladoras_fabrica2.html')

def olmaFH_perfiladoras_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/olmaFH_perfiladoras_fabrica2.html')

def sares1_perfiladoras_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/sares1_perfiladoras_fabrica2.html')

def sares2_perfiladoras_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/sares2_perfiladoras_fabrica2.html')

def pintura_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/pintura_fabrica2.html')

def pintura_fabrica2_po3(request):
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/maquinas_pintura_F2/pinturapo3_F2.html')

def pintura_fabrica2_po4(request):
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/maquinas_pintura_F2/pinturapo4_F2.html')

def fabrica3(request):
    return render(request, 'fabrica_3/fabrica3.html')

def prensa_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/prensa_fabrica3.html')

def fagor_prensa_F3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/maquinas_prensa_F3/fagor_prensa_F3.html')

def Aita_prensa_F3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/maquinas_prensa_F3/Aita_prensa_F3.html')

def perfiladora_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/perfiladora_fabrica3.html')

def jundiai_perfiladorasF3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/jundiai_perfiladorasF3.html')

def sares3_perfiladorasF3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/sares3_perfiladorasF3.html')

def sares4_perfiladorasF3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/sares4_perfiladorasF3.html')

def pintura_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/pintura_F3/pintura_fabrica3.html')

def pinturaliquidaF3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/pintura_F3/maquinas_pintura_F3/pinturaliquidaF3.html')








