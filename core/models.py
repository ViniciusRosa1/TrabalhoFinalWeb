from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from stdimage.models import StdImageField # type: ignore
from django.contrib.auth.models import User
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True) # Só será adicionado quando um novo elemento for criado.
    modificado = models.DateField('Atualiação', auto_now=True) # toda vez que esse obj for modificado, será atualizado esse elemento
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True

    
class Plano(Base):
    PLANO_CHOICE = (
        ('1', 'Uma aula semanal'),
        ('2', 'Duas aulas semanais'),
        ('3', 'Três aulas semanais')
    )
    
    nome = models.CharField('Nome', max_length=20, choices=PLANO_CHOICE)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        
    def __str__(self):
        return self.nome

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    
    servico = models.CharField('Serviço', max_length=30)
    descricao = models.TextField('Descrição', max_length=100)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        
    def __str__(self):
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=40)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo
    
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=40)
    cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    hora_trabalhadas = models.IntegerField('Horas/Semana')
    bio = models.TextField('Bio', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations= {'thumb': {'width': 480, 'heigth': 480,'crop': True}})
    face = models.CharField('Facebook', max_length=100, default='#')
    insta = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        
    def __str__(self):
        return self.nome
    
    
class Paciente(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=128)
    telefone = models.CharField('Telefone', max_length=20)
    plano = models.ForeignKey(Plano, verbose_name='Plano', on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, verbose_name='Serviço', on_delete=models.CASCADE,default=1)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        
    def __str__(self):
        return self.nome
    
class FichaAvaliacao(Base):
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    data = models.DateField('Data', auto_now_add=True)
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=0)
    altura = models.DecimalField('Altura', max_digits=5, decimal_places=0)
    imc = models.DecimalField('IMC', max_digits=5, decimal_places=1)
    gordura = models.DecimalField('Gordura', max_digits=5, decimal_places=0)
    observacoes = models.TextField('Observações', max_length=100)
    
    class Meta:
        verbose_name = 'Ficha de Avaliação'
        verbose_name_plural = 'Fichas de Avaliação'
        
    def __str__(self):
        return f'Ficha de Avaliação - {self.paciente.nome}'
    
class Boleto(Base):
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    data = models.DateField('Data', auto_now_add=True)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    data_vencimento = models.DateField('Vencimento')
    pago = models.BooleanField('Pago', default=False)
    
    class Meta:
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'
        
    def __str__(self):
        return f'Boleto - {self.paciente.nome} - {self.data_vencimento}'
           
class FichaTreino(Base):
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    data = models.DateField('Data', auto_now_add=True)
    exercicio = models.CharField('Exercício', max_length=100)
    series = models.IntegerField('Séries')
    repeticoes = models.IntegerField('Repetições')
    carga = models.DecimalField('Carga', max_digits=5, decimal_places=0)
    observacoes = models.TextField('Observações', max_length=100)
    
    class Meta:
        verbose_name = 'Ficha de Treino'
        verbose_name_plural = 'Fichas de Treino'
        
    def __str__(self):
        return f'Ficha de Treino - {self.paciente.nome}'
    
    def save(self, *args, **kwargs):
        self.valor = self.paciente.plano.preco
        super().save(*args, **kwargs)




class Agendamento(Base):
    HORA_CHOICES = [(f'{hour:02}:00', f'{hour:02}:00') for hour in range(7, 19)]
    
    data = models.DateField('Data')
    hora = models.CharField('Hora', max_length=5, choices=HORA_CHOICES)
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=20, default='Agendado')
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        unique_together = ('data', 'hora', 'paciente')
        
    def __str__(self):
        return f'{self.data} - {self.hora} - {self.paciente.nome}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)