from django.urls import path
from .views import IndexView, logIn, AreaPacienteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', logIn.as_view(), name='login'),
    path('area_paciente/', AreaPacienteView.as_view(), name='area_paciente')
]
