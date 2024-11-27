from django.shortcuts import render
from aplicacao.models import Cadastros
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LogoutView(View):

    def get(self, request):
        if request.method == "GET":
            return render (request, 'logout.html')
class LoginView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'login.html')
        
    def post(self, request):
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('aplicacao:home')

            return render(request, 'login.html')
        
class SucessoView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'sucesso.html')
        
class UsuariosView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'usuarios.html')

class CadastrarUsuarioView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'cadastrar_usuario.html')
        
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')

            if password == password_confirm:
                User.objects.create_user(username=username, password=password)
                return redirect('usuarios:login')
            
class CadastrarPublicoView(View):

    def get (self, request):
        if request.method == "GET":
            return render (request, 'cadastrar_publico.html')
        
    def post(self, request):

        if request.method == "POST":

            nome = request.POST.get('formNome')
            idade = request.POST.get('formIdade')
            cpf = request.POST.get('formCpf')
            celular = request.POST.get('formCelular')
            cep = request.POST.get('formCep')
            cidade = request.POST.get('formCidade')
            bairro = request.POST.get('formBairro')
            rua = request.POST.get('formRua')
            numero = request.POST.get('formNumero')
            complemento = request.POST.get('formComplemento')

            skillCostura = request.POST.get('nameSkillCostura') == 'on'
            skillGerenciamento = request.POST.get('nameSkillGerenciamento') == 'on'
            skillPintura = request.POST.get('nameSkillPintura') == 'on'

            try:
                usuario_responsavel = User.objects.get(username='GerenteFabrica') #costumizar?
            except User.DoesNotExist:
                return redirect('usuarios:cadastrar_publico')
            
            cadastro = Cadastros(nome = nome, idade = idade, cpf = cpf, celular = celular, cep = cep, cidade = cidade, bairro = bairro, rua = rua, numero = numero, complemento = complemento, skillCostura = skillCostura, skillGerenciamento = skillGerenciamento, skillPintura = skillPintura, usuario=usuario_responsavel)

            cadastro.save()

            return redirect('usuarios:sucesso')