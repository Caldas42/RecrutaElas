from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('cadastrar', views.CadastrarView.as_view(), name='cadastrar'),
    path('visualizar/<int:id>/', views.VisualizarCadastroView.as_view(), name='visualizar_cadastros'),
    path('excluir/<int:id>/', views.DeletarCadastroView.as_view(), name='excluir'),
    path('editar/<int:id>/', views.EditarCadastroView.as_view(), name='editar'),
    path('gerenciar_skills/<int:id>/', views.GerenciarSkillsView.as_view(), name='gerenciar_skills')
]
