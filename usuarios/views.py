from django.shortcuts import render
from aplicacao.models import Cadastros
from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'login.html')
        
class SucessoView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'sucesso.html')
        
class UsuariosView(View):

    def get(self, request):
        if request.method == "GET":
            return render(request, 'usuarios.html')

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

            cadastro = Cadastros(nome = nome, idade = idade, cpf = cpf, celular = celular, cep = cep, cidade = cidade, bairro = bairro, rua = rua, numero = numero, complemento = complemento, skillCostura = skillCostura, skillGerenciamento = skillGerenciamento, skillPintura = skillPintura)

            cadastro.save()

            return redirect('usuarios:sucesso')