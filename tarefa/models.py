from django.db import models
from django.utils import timezone


class ProjetoUsuario(models.Model):
    projeto = models.ForeignKey('Projeto')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.projeto)

class Usuario(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)
    senha = models.CharField('email', max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)

class Projeto(models.Model):
    nome = models.CharField('nome', max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)

class Tarefa(models.Model):
    nome = models.CharField('nome', max_length=200)
    dataEHoraDeInicio = models.DateTimeField('dataEHoraDeInicio', default=timezone.now)
    projeto = models.ForeignKey('Projeto')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.nome)
