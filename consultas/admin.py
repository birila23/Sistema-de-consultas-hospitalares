from django.contrib import admin
from .models import Consulta
from .calculo_consulta import recalcular_horarios

@admin.register(Consulta) #Registra o modelo Consulta no admin
class ConsultaAdmin(admin.ModelAdmin):
    # Campos que aparecerão no formulário de criação
    fields = ('paciente','data', 'descricao')

    # Campos só de leitura no admin (opcional, se quiser mostrar mas não editar)
    readonly_fields = ('horario_estimado', 'criado_em')

    # Campos exibidos na lista do admin
    list_display = ('data', 'descricao', 'paciente', 'horario_estimado', 'criado_em')

    # Opcional: se quiser que apareça filtros no admin
    list_filter = ('data',)

    # Opcional: para pesquisar pela descrição
    search_fields = ('descricao',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        recalcular_horarios(data_consultas=obj.data)