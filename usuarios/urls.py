from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastrar_publico/', views.CadastrarPublicoView.as_view(), name='cadastrar_publico'),
    path('usuarios/', views.UsuariosView.as_view(), name='usuarios'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sucesso/', views.SucessoView.as_view(), name='sucesso'),
]
