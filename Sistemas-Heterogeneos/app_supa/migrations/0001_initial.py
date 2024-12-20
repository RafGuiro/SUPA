# Generated by Django 5.1.3 on 2024-11-27 06:12

import app_supa.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medico",
            fields=[
                (
                    "nome",
                    models.CharField(max_length=255, verbose_name="Nome Completo"),
                ),
                (
                    "cpf",
                    models.CharField(
                        max_length=11,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="CPF",
                    ),
                ),
                (
                    "especialidade",
                    models.CharField(max_length=100, verbose_name="Especialidade"),
                ),
                ("contato", models.CharField(max_length=15, verbose_name="Contato")),
            ],
            options={
                "verbose_name": "Médico",
                "verbose_name_plural": "Médicos",
            },
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "nome",
                    models.CharField(max_length=255, verbose_name="Nome Completo"),
                ),
                (
                    "cpf",
                    models.CharField(
                        max_length=11,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        validators=[app_supa.models.validar_cpf],
                        verbose_name="CPF",
                    ),
                ),
                (
                    "cartao_sus",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Nº Cartão SUS"
                    ),
                ),
                (
                    "data_nascimento",
                    models.DateField(verbose_name="Data de Nascimento"),
                ),
                (
                    "contato",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\+?1?\\d{9,15}$",
                                message="Número de telefone inválido.",
                            )
                        ],
                        verbose_name="Contato",
                    ),
                ),
                (
                    "observacoes",
                    models.TextField(blank=True, null=True, verbose_name="Observações"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Última Atualização"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AgendamentoConsulta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "prioridade",
                    models.CharField(
                        choices=[
                            ("baixa", "Baixa"),
                            ("media", "Média"),
                            ("alta", "Alta"),
                            ("urgente", "Urgente"),
                        ],
                        max_length=10,
                        verbose_name="Prioridade",
                    ),
                ),
                (
                    "data",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data da Consulta"
                    ),
                ),
                (
                    "horario",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Horário da Consulta"
                    ),
                ),
                (
                    "profissional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_supa.medico",
                        verbose_name="Médico",
                    ),
                ),
                (
                    "cartao_sus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_supa.paciente",
                        to_field="cartao_sus",
                        verbose_name="Nº Cartão SUS",
                    ),
                ),
            ],
            options={
                "verbose_name": "Agendamento de Consulta",
                "verbose_name_plural": "Agendamentos de Consultas",
            },
        ),
    ]
