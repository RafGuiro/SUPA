from django.db import models
from django.core.validators import RegexValidator

class Paciente(models.Model):
    nome = models.TextField(
        max_length=255, 
        verbose_name="Nome Completo"
    )
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        unique=True, 
        verbose_name="CPF"
    )
    cartao_sus = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Nº Cartão SUS"
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento"
    )
    contato = models.CharField(
        max_length=15, 
        blank=True,
        null=True,
        verbose_name="Contato",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Número de telefone inválido.")]
    )
    observacoes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observações"
    )
    
class Medico(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome Completo"
    )
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        unique=True, 
        verbose_name="CPF"
    )
    especialidade = models.CharField(
        max_length=100, 
        verbose_name="Especialidade"
    )
    contato = models.CharField(
        max_length=15, 
        verbose_name="Contato"
    )
    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
    def __str__(self):
        return f"{self.nome} ({self.especialidade})"

class AgendamentoConsulta(models.Model):
    cartao_sus = models.ForeignKey(
        'Paciente',
        on_delete=models.CASCADE,
        to_field='cartao_sus',
        verbose_name="Nº Cartão SUS"
    )
    profissional = models.ForeignKey(
        'Medico',
        on_delete=models.CASCADE,
        verbose_name="Médico"
    )
    prioridade = models.CharField(
        max_length=10,
        choices=[
            ('baixa', 'Baixa'),
            ('media', 'Média'),
            ('alta', 'Alta'),
            ('urgente', 'Urgente')
        ],
        verbose_name="Prioridade"
    )
    data = models.DateField(verbose_name="Data da Consulta")
    horario = models.TimeField(verbose_name="Horário da Consulta")

    class Meta:
        verbose_name = "Agendamento de Consulta"
        verbose_name_plural = "Agendamentos de Consultas"

    def __str__(self):
        return f"{self.cartao_sus.nome} - {self.profissional.especialidade} - {self.data} {self.horario}"
