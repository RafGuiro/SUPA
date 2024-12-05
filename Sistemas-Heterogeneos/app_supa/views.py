from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medico, AgendamentoConsulta
from django.contrib.auth import aauthenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
import re


def login_view(request):
    next_url = request.GET.get('next', 'home')  # Pega o parâmetro 'next' ou usa a home como padrão
    return redirect(next_url)

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Validação básica
        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect('register')

        # Criando o usuário
        user = User.objects.create_user(
            username=email,  # O Django usa 'username' internamente
            first_name=name,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'Tela-Cadastro/index.html')

@login_required
def home(request):
    # Buscando todos os agendamentos
    agendamentos = AgendamentoConsulta.objects.all()

    # Passando os agendamentos para o template
    return render(request, 'Tela-Home/index.html', {'agendamentos': agendamentos})

def paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome-pac')
        cpf = request.POST.get('cpf-pac').replace('.', '').replace('-', '')  # Remover pontos e traços
        cartao_sus = request.POST.get('csus')
        data_nascimento = request.POST.get('data-nascimento')
        contato = request.POST.get('contato-pac')
        observacoes = request.POST.get('observacoes', '')

        # Verifica se o CPF ou cartão SUS já existe
        if Paciente.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado.")
        elif Paciente.objects.filter(cartao_sus=cartao_sus).exists():
            messages.error(request, "Cartão SUS já cadastrado.")
        else:
            # Criar e salvar o paciente
            paciente = Paciente(
                nome=nome,
                cpf=cpf,
                cartao_sus=cartao_sus,
                data_nascimento=data_nascimento,
                contato=contato,
                observacoes=observacoes
            )
            paciente.save()
            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect('/home')
    return render(request, 'Tela-Cad_paciente/index.html')

def medico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf').replace('.', '').replace('-', '')  # Remove pontos e traços
        especialidade = request.POST.get('especialidade')
        contato = request.POST.get('contato')

        # Validando o CPF
        if not re.match(r'^\d{11}$', cpf):
            messages.error(request, "CPF inválido. Deve conter apenas números.")
            return render(request, 'cadastro_medico.html')

        # Verificando se o CPF já está cadastrado
        if Medico.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado.")
            return render(request, 'cadastro_medico.html')

        # Criando o médico
        medico = Medico(nome=nome, cpf=cpf, especialidade=especialidade, contato=contato)
        medico.save()
        messages.success(request, "Médico cadastrado com sucesso!")
        return redirect('/home')  # Redireciona para a página inicial após o cadastro

    return render(request, 'Tela-Cad_medico/index.html')

def agendamento(request):
    if request.method == 'POST':
        cartao_sus = request.POST.get('csus')
        cpf = request.POST.get('profissional')
        prioridade = request.POST.get('prioridade')
        data = request.POST.get('data')  # Pode vir vazio
        horario = request.POST.get('horario')  # Pode vir vazio

        # Verificando se o paciente com o Cartão SUS existe
        try:
            paciente = Paciente.objects.get(cartao_sus=cartao_sus)
        except Paciente.DoesNotExist:
            messages.error(request, "Paciente não encontrado com o Cartão SUS informado.")
            return redirect('Tela-Agend/index.html')

        # Verificando se o médico escolhido existe
        try:
            profissional = Medico.objects.get(cpf=cpf)
        except Medico.DoesNotExist:
            messages.error(request, "Médico não encontrado.")
            return redirect('Tela-Agend/index.html')

        # Se os campos de data ou horário não foram preenchidos, podem ser deixados em branco
        agendamento = AgendamentoConsulta(
            cartao_sus=paciente,
            profissional=profissional,
            prioridade=prioridade,
            data=data if data else None,  # Deixa em branco se não for fornecido
            horario=horario if horario else None  # Deixa em branco se não for fornecido
        )
        agendamento.save()

        messages.success(request, "Consulta agendada com sucesso!")
        return redirect('/home')

    # Buscando todos os médicos para exibir no select
    medicos = Medico.objects.all()
    return render(request, 'Tela-Agend/index.html', {'medicos': medicos})

def deletar(request, agendamento_id):
    # Busca o agendamento pelo id
    agendamento = get_object_or_404(AgendamentoConsulta, id=agendamento_id)
    
    # Deleta o agendamento
    agendamento.delete()
    
    # Exibe uma mensagem de sucesso
    messages.success(request, "Agendamento deletado com sucesso!")
    
    # Redireciona de volta para a página home
    return redirect('home')