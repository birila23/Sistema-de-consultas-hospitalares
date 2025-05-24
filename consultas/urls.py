from django.urls import path, include

from .views import ConsultaCreateView, ConsultaCreateViewUpDest

urlpatterns = [
    path('consultas/', ConsultaCreateView.as_view(), name='consultas'),
    path('consultas/<int:pk>', ConsultaCreateViewUpDest.as_view(), name='consultass')
]