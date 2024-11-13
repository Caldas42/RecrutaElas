from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Cadastros

class HomeView(View):
    def get (self, request):
        cadastro = Cadastros.objects.all()

        ctx = {
            'todos_cadastros': cadastro,
        }

        return render(request, 'home.html', ctx)
    
class CadastrarView(View):
    def get (self, request):
        if request.method == "GET":
            return render (request, 'cadastrar.html')
        
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

            return redirect('aplicacao:home')

class VisualizarCadastroView(View):
    def get (self, request, id):
        ctx = {'cadastro':Cadastros.objects.filter(id=id).first()}

        return render (request, 'visualizar_cadastro.html', ctx)
    
class DeletarCadastroView(View):
    def post(self, request, id):
        cadastro = get_object_or_404(Cadastros, id=id)
        cadastro.delete()
        return redirect('aplicacao:home')
    
class EditarCadastroView(View):

    def get(self, request, id):

        cadastro_obj = get_object_or_404(Cadastros, id=id)
        return render(request, 'editar.html', {'cadastro': cadastro_obj})

    def post(self, request, id):

        cadastro_obj = get_object_or_404(Cadastros, id=id)
        cadastro_obj.nome = request.POST.get('formNome')
        cadastro_obj.idade = request.POST.get('formIdade')
        cadastro_obj.cpf = request.POST.get('formCpf')
        cadastro_obj.celular = request.POST.get('formCelular')
        cadastro_obj.cep = request.POST.get('formCep')
        cadastro_obj.cidade = request.POST.get('formCidade')
        cadastro_obj.bairro = request.POST.get('formBairro')
        cadastro_obj.rua = request.POST.get('formRua')
        cadastro_obj.numero = request.POST.get('formNumero')
        cadastro_obj.complemento = request.POST.get('formComplemento')

        cadastro_obj.skillCostura = request.POST.get('nameSkillCostura') == 'on'
        cadastro_obj.skillGerenciamento = request.POST.get('nameSkillGerenciamento') == 'on'
        cadastro_obj.skillPintura = request.POST.get('nameSkillPintura') == 'on'

        cadastro_obj.save()

        return redirect('aplicacao:visualizar_cadastros', id=cadastro_obj.id)

class GerenciarSkillsView(View):
    def get(self, request):
        return render(request, 'gerenciar_skills.html')
    
    def post(self, request):
        skillSelecionada = request.POST.get('nameSelectBox')

        if skillSelecionada:
            cadastros_filtrados = Cadastros.objects.filter(**{skillSelecionada: True})
        else:
            cadastros_filtrados = Cadastros.objects.all()

        return render(request, 'gerenciar_skills.html', {'cadastrosFiltrados': cadastros_filtrados})