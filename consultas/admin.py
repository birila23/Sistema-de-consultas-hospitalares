from django.contrib import admin
from .models import Consulta

@admin.register(Consulta) #Registra o modelo Consulta no admin
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data','criado_em', 'horario_estimado', 'descricao') #Quais campos aparecem na lista principal
    list_filter = ('data',)
    search_fields = ('paciente','descricao') #Adiciona busca por nome de paciente ou descrição