from django.db import models
from datetime import date
from ..enumerations import LinguagemProgramacao

class ProjetoManager(models.Manager):
    def listar_projetos_linguagem(self, inicio: date, fim: date, linguagem):
        if not isinstance(inicio, date) or not isinstance(fim, date):
            raise TypeError("Inicio e fim devem ser datas")

        if inicio > fim:
            raise ValueError("A data inicial não pode ser posterior a data final")

        if linguagem not in LinguagemProgramacao.values:
            raise ValueError("Linguagem de programação inválida")

        return self.get_queryset().filter(
            tarefas__criacao__date__range=(inicio, fim),
            tarefas__linguagem=linguagem,
        ).distinct()