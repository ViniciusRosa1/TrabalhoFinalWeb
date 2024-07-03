# TrabalhoFinalWeb

Projeto Final para a disciplina de desenvolvimento de sistemas web realizada na UFSC.

# Sobre o porjeto

Projeto de um website para uma clínica de Pilates visando seu melhor gerenciamento com seus funcionários e pacientes.

# Configuração do Ambiente de Desenvolvimento:

1. Clone este repositório: ```cli git clone https://github.com/ViniciusRosa1/TrabalhoFinalWeb.git ```

2. Crie e ative um ambiente virtual:
```cli
virtualenv env
```

3. Instale as dependências e criar txt com requirements:
```cli
  pip install -r requirements.txt
  pip freeze > requirements.txt
```
4. Crie um superusuário para acessar o painel de administração em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/):
```cli
  python manage.py createsuperuser
```
 
5. Inicie o servidor de desenvolvimento:
```cli
  python manage.py runserver
```
