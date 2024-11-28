from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from aplicacao.models import Cadastros

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
            email = request.POST.get('formEmail')
            cep = request.POST.get('formCep')
            cidade = request.POST.get('formCidade')
            bairro = request.POST.get('formBairro')
            rua = request.POST.get('formRua')
            numero = request.POST.get('formNumero')
            complemento = request.POST.get('formComplemento')
            escolaridade = request.POST.get('formEscolaridade')
            experiencia = request.POST.get('formExperiencia')
            disponibilidade = request.POST.get('formDisponibilidade')
            interesse = request.POST.get('formInteresse')

            imagem = request.FILES.get('formImagem')

            skillCostura = request.POST.get('nameSkillCostura') == 'on'
            skillGerenciamento = request.POST.get('nameSkillGerenciamento') == 'on'
            skillPintura = request.POST.get('nameSkillPintura') == 'on'
            skillDesign = request.POST.get('nameSkillDesign') == 'on'
            skillCriatividade = request.POST.get('nameSkillCriatividade') == 'on'
            skillAtendimento = request.POST.get('nameSkillAtendimento') == 'on'
            skillVendas = request.POST.get('nameSkillVendas') == 'on'
            skillLimpeza = request.POST.get('nameSkillLimpeza') == 'on'

            try:
                usuario_responsavel = User.objects.get(username='GerenteFabrica') #costumizar?
            except User.DoesNotExist:
                return redirect('usuarios:cadastrar_publico')
            
            cadastro = Cadastros(nome = nome, 
                                 idade = idade, 
                                 cpf = cpf, 
                                 celular = celular, 
                                 email = email, 
                                 cep = cep, 
                                 cidade = cidade, 
                                 bairro = bairro, 
                                 rua = rua, 
                                 numero = numero,
                                 complemento = complemento, 
                                 escolaridade = escolaridade,
                                 experiencia = experiencia,
                                 disponibilidade = disponibilidade,
                                 interesse = interesse,
                                 skillCostura = skillCostura, 
                                 skillGerenciamento = skillGerenciamento, 
                                 skillPintura = skillPintura, 
                                 skillDesign = skillDesign,
                                 skillCriatividade = skillCriatividade,  
                                 skillAtendimento = skillAtendimento,
                                 skillVendas = skillVendas,
                                 skillLimpeza = skillLimpeza,   
                                 usuario=usuario_responsavel, 
                                 imagem=imagem)

            cadastro.save()

            return redirect('usuarios:sucesso')
        
class Deletar_Cypress(View):

    def get(self, request):
        return render(request, 'excluir_cypress.html')

    def post(self, request):
        User.objects.all().delete()
        return redirect('login')