from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Servico, Funcionario, Paciente, FichaAvaliacao, Boleto, FichaTreino, Agendamento, Plano
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all() 
        context['planos'] = Plano.objects.all()
        
        return context
    
class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"VocÊ está logado como {username}")
                    return redirect('area_paciente')
                else:
                    messages.error(request, "ERRO")
            else:
                messages.error(request, 'Usuário ou senha inválidos')
        form = LoginUserForm()
        return render(request, "templates/login.html", {'form': form})
                    
class AreaPacienteView(LoginRequiredMixin, TemplateView):
    template_name = 'area_paciente.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            paciente = self.request.user.paciente
            context['paciente'] = paciente
            context['fichas_avaliacao'] = FichaAvaliacao.objects.filter(paciente=paciente)
            context['boletos'] = Boleto.objects.filter(paciente=paciente)
            context['fichas_treino'] = FichaTreino.objects.filter(paciente=paciente)
            context['agendamentos'] = Agendamento.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            context['error'] = "Paciente não encontrado. Verifique se o usuário está associado a um paciente."
        return context


    