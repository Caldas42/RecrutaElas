from django.urls import path
from .models import cadastros, Comentario
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('cadastrar', views.CadastrarView.as_view(), name='cadastrar'),
    path('visualizar/<int:id>/', views.VisualizarCadastroView.as_view(), name='visualizar_cadastros'),
    path('adicionar_comentario/', views.adicionar_comentario, name='adicionar_comentario'),
]
