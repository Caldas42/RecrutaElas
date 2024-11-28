from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    path('cadastrar/', views.CadastrarView.as_view(), name='cadastrar'),
    path('visualizar/<int:id>/', views.VisualizarCadastroView.as_view(), name='visualizar_cadastros'),
    path('excluir/<int:id>/', views.DeletarCadastroView.as_view(), name='excluir'),
    path('editar/<int:id>/', views.EditarCadastroView.as_view(), name='editar'),

    path('gerenciar_skills/', views.GerenciarSkillsView.as_view(), name='gerenciar_skills'),
    path('gerenciar_pastas/', views.GerenciarPastasView.as_view(), name='gerenciar_pastas'),
    path('criar_pasta/', views.CriarPastaView.as_view(), name='criar_pasta'),
    path('pastas/detalhes/<int:id>/', views.DetalhesPastaView.as_view(), name='detalhes_pasta'),
    path('deletar_pasta/<int:id>/', views.DeletarPastaView.as_view(), name='deletar_pasta'),

    path('registrar_brinquedo/', views.RegistrarBrinquedoView.as_view(), name = 'registrar_brinquedo'),
    path('home_brinquedos/', views.HomeBrinquedosView.as_view(), name = 'home_brinquedos'),
    path('editar_brinquedo/<int:id>/', views.EditarBrinquedoView.as_view(), name = 'editar_brinquedo'),
    path('deletar_brinquedo/<int:id>/', views.DeletarBrinquedoView.as_view(), name = 'deletar_brinquedo'),
    path('visualizar_brinquedo/<int:id>/', views.VisualizarBrinquedoView.as_view(), name = 'visualizar_brinquedo'),
    path('home_cadastros/', views.HomeCadastrosView.as_view(), name='home_cadastros'),

    path('pastas/detalhes/<int:id>/', views.DetalhesPastaView.as_view(), name='detalhes_pasta'),
    path('pastas/adicionar_colaboradoras/<int:pasta_id>/', views.AdicionarColaboradorasView.as_view(), name='adicionar_colaboradoras'),

]
