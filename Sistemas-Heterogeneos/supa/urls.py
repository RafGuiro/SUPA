from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from app_supa import views

urlpatterns = [
    path('', lambda request: redirect('login'), name='index'),
    #Tela de Cadastro
    path('register/', views.register, name='register'),
    #Tela de login
    path('login/', auth_views.LoginView.as_view(template_name='Tela-Login/index.html'), name='login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #Telas de Interação
    path('home/',views.home,name="home"),
    path('agendamento/',views.agendamento,name="agendamento"),
    path('paciente/',views.paciente,name="paciente"),
    path('medico/',views.medico,name="medico"),
    #Deleta Paciente
    path('deletar/<int:agendamento_id>/', views.deletar, name='deletar'),  
]

