from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from .enumerations import TipoProjeto, Status, LinguagemProgramacao
from django.core.exceptions import ValidationError
# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)]
    )
    codigo = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(5)]
    )
    tipo_projeto = models.CharField(
        max_length=30,
        choices=TipoProjeto.choices
    )
    cliente = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)]
    )
    gerente = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)]
    )
    ativo = models.BooleanField(
        default=True
    )
    inicio = models.DateField(
        
    )
    fim = models.DateField(
        blank=True,
        null=True
    )
    previsao_termino = models.DateField(

    )
    orcamento = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def clean(self):
        super().clean()
        if self.inicio and self.previsao_termino:
            if self.previsao_termino < self.inicio:
                raise ValidationError({
                    "previsao_termino": "A previsão não pode ser anterior ao inicio."
                })
            
        if self.inicio and self.fim:
            if self.inicio > self.fim:
                raise ValidationError({
                    "fim": "O fim não pode ser anterior ao inicio."
                })

    def __str__(self):
        inicio = self.inicio.strftime("%d/%m/%Y") if self.inicio else "sem data"
        previsao = (
            self.previsao_termino.strftime("%d/%m/%Y")
            if self.previsao_termino else "sem data"
        )
        return f"{self.cliente} - {self.nome} - {self.tipo_projeto} - {self.orcamento} - {inicio} - {previsao}"

class Tarefa(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    titulo = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)]
    )
    descricao = models.TextField(
        max_length=1000,
        blank=True,
        null=True
    )
    linguagem = models.CharField(
        max_length=30,
        choices=LinguagemProgramacao.choices
    )
    estimativa_horas = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    horas_registradas = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    prioridade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    status = models.CharField(
        max_length=30,
        choices=Status.choices
    )
    responsavel = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)]
    )
    criacao = models.DateTimeField(

    )
    conclusao = models.DateTimeField(
        blank=True,
        null=True,

    )

    def clean(self):
        super().clean()
        if self.conclusao and self.criacao:
            if self.conclusao < self.criacao:
                raise ValidationError({
                    "conclusao": "A conclusão não pode ser anterior à criação."
                })

        if self.projeto_id and self.criacao:    
            if self.criacao.date() < self.projeto.inicio:
                raise ValidationError({
                    "criacao": "A criação da tarefa não pode ser anterior ao início do projeto"
                })
        if self.projeto_id and self.pk is None:
            projeto_fechado  = not self.projeto.ativo or self.projeto.fim is not None

            if projeto_fechado:
                raise ValidationError({
                    "projeto": "Não é possivel criar tarefas em um projeto fechado"
                })

    def __str__(self):
        criacao_formatada = (
            self.criacao.strftime("%d/%m/%Y")
            if self.criacao else "sem data"
            )
        conclusao_formatada = (
            self.conclusao.strftime("%d/%m/%Y")
            if self.conclusao else "não concluida"
            ) 
        return f"{self.responsavel} - {self.linguagem} - {self.titulo} - {criacao_formatada} - {conclusao_formatada} - {self.estimativa_horas} - {self.status}"