from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastrar_publico/', views.CadastrarPublicoView.as_view(), name='cadastrar_publico'),
    path('', views.UsuariosView.as_view(), name='usuarios'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sucesso/', views.SucessoView.as_view(), name='sucesso'),
    path('cadastrar_usuario/', views.CadastrarUsuarioView.as_view(), name='cadastrar_usuario'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
