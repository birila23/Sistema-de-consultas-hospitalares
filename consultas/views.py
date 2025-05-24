from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Consulta
from .serializers import ConsultaSerializer
from .calculo_consulta import recalcular_horarios


class ConsultaCreateView(generics.ListCreateAPIView):
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Usuário vê apenas suas consultas
        return Consulta.objects.filter(paciente=self.request.user)

    def perform_create(self, serializer):
        # Se for admin, deixa ele informar o paciente; senão, força o usuário logado
        if not self.request.user.is_staff:
            consulta = serializer.save(paciente=self.request.user)
        else:
            consulta = serializer.save()
        
        recalcular_horarios(consulta.data)

class ConsultaCreateViewUpDest(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_staff):
            return Consulta.objects.all()
        return Consulta.objects.filter(paciente=self.request.user)
    
    def perform_update(self, serializer):
        consulta = serializer.save()
        recalcular_horarios(consulta.data)
    
    def perform_destroy(self, instance):
        # O código salva a data da consulta antes de deletar, 
        # porque vai precisar disso para recalcular os horários do restante.
        data = instance.data
        instance.delete()
        recalcular_horarios(data)