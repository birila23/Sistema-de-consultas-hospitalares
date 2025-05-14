from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE) #quem agendou, é um usuario do USER.
    data = models.DateField() #O dia da consulta
    criado_em = models.DateTimeField(auto_now_add = True) #timestamps automáticos de criação
    horario_estimado = models.TimeField(null=True, blank=True) #Hora estimada que a pessoa vai ser atendida
    descricao = models.TextField(blank= True) # espaço opcional para descrição da consulta.

    def __str__(self):
        return f"{self.paciente.username} - {self.data} às {self.horario_estimado}"
    
        