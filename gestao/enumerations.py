from django.db import models

class TipoProjeto(models.TextChoices):
    WEB = "WEB", "Desenvolvimento Web"
    MOBILE = "MOBILE", "Aplicativo de Celular"
    DESKTOP = "DESKTOP", "Aplicação Desktop"
    API = "API", "Web Services/API"
    LIBRARY = "LIBRARY", "Biblioteca/SDK"
    DATA_SCIENCE = "DATA_SCIENCE", "Projeto de Ciência de Dados"
    AI = "AI", "Inteligência Artificial"

class Status(models.TextChoices):
    PENDING = "PENDING", "Pendente"
    DOING = "DOING", "Em andamento"
    DONE = "DONE", "Concluido"
    BLOCKED = "BLOCKED", "Bloqueado"
    DELAYED = "DELAYED", "Atrasado"

class LinguagemProgramacao(models.TextChoices):
    PYTHON = "PYTHON", "Python"
    JS = "JS", "JavaScript"
    JAVA = "JAVA", "Java"
    CSHARP = "CSHARP", "C#"
    CPLUSPLUS = "CPLUSPLUS", "C++"
    C = "C", "C"
    PHP = "PHP", "Php"
    DART = "DART", "Dart"