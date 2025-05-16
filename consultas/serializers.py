#Converte o modelo Consulta em JSON e valida dados.
from .models import Consulta
from rest_framework import serializers

#Esse serializer transforma o modelo consulta em JSON, para usar a API rest.
class ConsultaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Consulta
        fields = ['id', 'data', 'descricao', 'horario_estimado', 'criado_em', 'paciente']
        read_only_fields = ['id', 'horario_estimado', 'criado_em']