from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Cargo, Servico, Funcionario, Plano, Paciente, FichaAvaliacao, Boleto, FichaTreino, Agendamento

# Register your forms here.
from .forms import AgendamentoForm

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')
    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'hora_trabalhadas', 'ativo', 'modificado')
    
@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ativo', 'modificado')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'plano', 'ativo', 'modificado')
    
@admin.register(FichaAvaliacao)
class FichaAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'peso', 'altura', 'imc', 'gordura', 'observacoes', 'ativo', 'modificado')
    
@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data', 'valor', 'data_vencimento', 'pago', 'ativo', 'modificado')

@admin.register(FichaTreino)
class FichaTreinoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'exercicio', 'series', 'repeticoes', 'carga', 'observacoes', 'ativo', 'modificado')
    
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    form = AgendamentoForm
    list_display = ('data', 'hora', 'paciente', 'status', 'ativo', 'modificado')