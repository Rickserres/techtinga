from django.db import models

class Tarefa_manager(models.Manager):
    def listar_tarefas_projeto(self, projeto):
        from ..models import Projeto

        if not isinstance(projeto, Projeto):
            raise TypeError("Informe um objeto Projeto.")

        if projeto.pk is None:
            raise ValueError("O projeto precisa estar salvo.")

        return self.get_queryset().filter(
            projeto=projeto
        ).order_by("responsavel", "status", "criacao")

    def listar_tarefas_colaborador(self, responsavel: str):
        if not isinstance(responsavel, str):
            raise TypeError("O responsavel deve ser um texto")

        responsavel= responsavel.strip()

        if len(responsavel) < 3:
            raise ValueError("Informe o nome do responsável.")

        return self.get_queryset().filter(
            responsavel__iexact=responsavel
        ).order_by("status", "criacao")