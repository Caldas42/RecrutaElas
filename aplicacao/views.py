from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Cadastros, Pasta, Brinquedo
from django.contrib import messages


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
    
class GerenciarPastasView(View):
    def get(self, request):
        pastas = Pasta.objects.all()
        cadastros = Cadastros.objects.all()
        return render(request, 'gerenciar_pastas.html', {
            'pastas': pastas,
            'cadastros': cadastros,
        })

    def post(self, request):
        nome_pasta = request.POST.get('nomePasta')
        cadastros_selecionados = request.POST.getlist('cadastros')

        if nome_pasta:
            pasta = Pasta.objects.create(nome=nome_pasta)
            if cadastros_selecionados:
                pasta.cadastros.set(cadastros_selecionados)
            pasta.save()

        return redirect('aplicacao:gerenciar_pastas')

class CriarPastaView(View):
    def get(self, request):
        cadastros = Cadastros.objects.all()  # Todos os cadastros disponíveis
        return render(request, 'criar_pasta.html', {'cadastros': cadastros})

    def post(self, request):
        nome_pasta = request.POST.get('nomePasta')
        cadastros_selecionados = request.POST.getlist('cadastros')

        if nome_pasta:
            pasta = Pasta.objects.create(nome=nome_pasta)
            if cadastros_selecionados:
                pasta.cadastros.set(cadastros_selecionados)
            pasta.save()

        return redirect('aplicacao:gerenciar_pastas')

class DetalhesPastaView(View):
    def get(self, request, id):
        pasta = get_object_or_404(Pasta, id=id)
        # Passando as mulheres associadas à pasta
        ctx = {
            'pasta': pasta,
        }
        return render(request, 'detalhes_pasta.html', ctx)
    
class DeletarPastaView(View):
    def post(self, request, id):
        pasta = get_object_or_404(Pasta, id=id)
        pasta.delete()  # Deleta o objeto Pasta
        return redirect('aplicacao:gerenciar_pastas')

class HomeBrinquedosView(View):
    def get(self, request):
        
        brinquedo = Brinquedo.objects.all()

        ctx = { 'todos_brinquedos': brinquedo, }

        return render(request, 'home_brinquedos.html', ctx)

class RegistrarBrinquedoView(View):
    def get(self, request):
        return render(request, 'registrar_brinquedo.html')
    
    def post(self, request):

        brinquedo = Brinquedo()

        brinquedo.nome = request.POST.get('nameFormBrinquedoNome')
        brinquedo.categoria = request.POST.get('nameFormBrinquedoCategoria')
        brinquedo.materiais = request.POST.get('nameFormBrinquedoMateriais')
        brinquedo.tematica = request.POST.get('nameFormBrinquedoTematica')
        brinquedo.quantidade = request.POST.get('nameFormBrinquedoQuantidade')
        brinquedo.imagem = request.FILES.get('nameFormBrinquedoImagem')
        

        brinquedo.save()

        messages.success(request, 'Brinquedo adicionado com sucesso!')
        return redirect('aplicacao:home_brinquedos')
    
class VisualizarBrinquedoView(View):
    def get(self, request, id):
        ctx = {'brinquedo':Brinquedo.objects.filter(id=id).first()}

        return render (request, 'visualizar_brinquedo.html', ctx)
    
class DeletarBrinquedoView(View):
    def get(self, request, id):
        ctx = {'brinquedo':Brinquedo.objects.filter(id=id).first()}

        return render(request, 'deletar_brinquedo.html', ctx)

    def post(self, request, id):
        brinquedo = get_object_or_404(Brinquedo, id=id)
        brinquedo.delete()
        messages.success(request, 'Brinquedo deletado com sucesso!')
        return redirect('aplicacao:home_brinquedos')
    
class EditarBrinquedoView(View):

    def get(self, request, id):

        brinquedo = get_object_or_404(Brinquedo, id=id)
        return render(request, 'editar_brinquedo.html', {'brinquedo': brinquedo})

    def post(self, request, id):

        brinquedo = get_object_or_404(Brinquedo, id=id)
        
        brinquedo.nome = request.POST.get('nameFormBrinquedoNomeEdit')
        brinquedo.categoria = request.POST.get('nameFormBrinquedoCategoriaEdit')
        brinquedo.materiais = request.POST.get('nameFormBrinquedoMateriaisEdit')
        brinquedo.tematica = request.POST.get('nameFormBrinquedoTematicaEdit')
        brinquedo.quantidade = request.POST.get('nameFormBrinquedoQuantidadeEdit')

        brinquedo.save()

        messages.success(request, 'Brinquedo editado com sucesso!')
        return redirect('aplicacao:home_brinquedos', id = brinquedo.id)