from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente, Medico, AgendamentoConsulta
from django.core.exceptions import ObjectDoesNotExist


def login(request):
    return render(request,'Tela-Login/index.html')

def cadastro(request):
    return render(request,'Tela-Cadastro/index.html')

def paciente(request):
    if request.method == 'POST':
        # Criar novo paciente
        novo_paciente = Paciente()
        novo_paciente.nome = request.POST.get('nome-pac')
        novo_paciente.cpf = request.POST.get('cpf-pac')
        novo_paciente.csus = request.POST.get('csus')
        novo_paciente.data = request.POST.get('data-nascimento')
        novo_paciente.contato = request.POST.get('contato-pac')
        novo_paciente.obs = request.POST.get('observacoes')
        
        try:
            novo_paciente.save()
        except Exception as e:
            # Aqui você pode adicionar um tratamento de erro ou log
            print(f'Erro ao salvar paciente: {e}')

    pacientes = {
        'pacientes': Paciente.objects.all()
    }
    return render(request, 'Tela-Cad_paciente/index.html', pacientes)

def medico(request):
    return render(request, 'Tela-Cad_medico/index.html')

def agendamento(request):
    return render(request, 'Tela-Agend/index.html')

def home(request):
    return render(request,'Tela-Home/index.html')
