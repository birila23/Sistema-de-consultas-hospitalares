from datetime import datetime, time, timedelta
from .models import Consulta
"""
    data_consultas: datetime.date - o dia das consultas
    inicio: horário inicial do atendimento (ex: 08:00)
    duracao: duração média em minutos por paciente
"""
def recalcular_horarios(data_consultas, inicio=time(8, 0), duracao=15): 
    fila = Consulta.objects.filter(data = data_consultas).order_by('criado_em')
    horario_atual = datetime.combine(data_consultas, inicio)

    #ele já faz todas as consultas de uma vez 
    for consulta in fila:
        consulta.horario_estimado = horario_atual.time
        consulta.save()
        horario_atual += timedelta(minutes=duracao)

