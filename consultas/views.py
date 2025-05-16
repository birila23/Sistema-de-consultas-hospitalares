#Controla o que pode ser feito (listar, criar, etc.).
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .calculo_consulta import recalcular_horarios
from .models import Consulta
from .serializers import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()  # Apenas usado no admin ou debug
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Garante que o paciente só veja suas próprias consultas
        return Consulta.objects.filter(paciente=self.request.user)

    def perform_create(self, serializer):
        # Salva a consulta com o paciente como o usuário logado
        consulta = serializer.save(paciente=self.request.user)

        # Recalcula os horários para o dia dessa nova consulta
        recalcular_horarios(data_consultas=consulta.data)