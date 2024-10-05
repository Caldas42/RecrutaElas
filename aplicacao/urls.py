from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.CadastrosView.as_view(), name = "home"),
    path('visualizar/<int:id>/', views.CadastroDetalhadoView.as_view(), name='visualizar_cadastros'),
    path('adicionar', views.AdicionarCadastro.as_view(), name='adicionar_cadastro'),
]
