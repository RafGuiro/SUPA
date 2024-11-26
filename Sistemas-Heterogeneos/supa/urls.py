from django.urls import path
from app_supa import views

urlpatterns = [
    #Tela de login
    path('', views.login, name="login"),
    #Tela de Cadastro
    path('cadastro/',views.cadastro,name="cadastro"),
    #Telas de Interação
    path('home/',views.home,name="home"),
    path('agendamento/',views.agendamento,name="agendamento"),
    path('paciente/',views.paciente,name="paciente"),
    path('medico/',views.medico,name="medico"),
]
