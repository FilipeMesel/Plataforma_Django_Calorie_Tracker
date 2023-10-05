
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Alimentos
from .forms import AlimentosForm

# Create your views here.
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'base_generic.html'  # Verifique se o nome corresponde ao arquivo correto.

@login_required
def home(request):
    user_id = request.user.id  # Obtém o ID do usuário logado
    user_name = request.user.username  # Obtém o nome do usuário logado
    context = {
        'user_id': user_id,
        'user_name': user_name,
    }
    return render(request, 'home.html', context)

@login_required
def cadastrar_entidade(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = AlimentosForm(request.POST)
        if form.is_valid():
            entidade = form.save(commit=False)
            entidade.user = user
            entidade.save()
            return redirect('home')  # Redirecione para a página de listagem de entidades
    else:
        form = AlimentosForm()

    return render(request, 'cadastro_entidade.html', {'form': form, 'user': user})

@login_required
def lista_alimentos(request, user_id):
    entidades = Alimentos.objects.filter(user_id=user_id)
    user = User.objects.get(id=user_id)

    qtd_cal = 0
    for entidade in entidades:
        qtd_cal += entidade.calorias

    return render(request, 'lista_alimentos.html', {'entidades': entidades, 'user': user, 'total_calorias': qtd_cal})