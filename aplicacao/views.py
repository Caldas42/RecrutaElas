from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Cadastros, Pasta, Brinquedo
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    def get (self, request):
        return render(request, 'home.html')

class HomeCadastrosView(LoginRequiredMixin, View):
    def get(self, request):
        
        cadastros = Cadastros.objects.filter(usuario=request.user).order_by('-id')

        ctx = {'cadastros': cadastros}

        return render(request, 'home_cadastros.html', ctx)
    
class CadastrarView(LoginRequiredMixin, View):
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

            imagem = request.FILES.get('formCadastroImagem')

            cadastro = Cadastros(nome = nome, idade = idade, cpf = cpf, celular = celular, cep = cep, cidade = cidade, bairro = bairro, rua = rua, numero = numero, complemento = complemento, skillCostura = skillCostura, skillGerenciamento = skillGerenciamento, skillPintura = skillPintura, usuario=request.user, imagem = imagem)

            cadastro.save()

            messages.success(request, 'Cadastro adicionado com sucesso!')

            return redirect('aplicacao:home_cadastros')

class VisualizarCadastroView(LoginRequiredMixin, View):
    def get (self, request, id):

        cadastro = get_object_or_404(Cadastros, id=id, usuario=request.user)  # Certifica-se que pertence ao usuário
        ctx = {'cadastro': cadastro}

        return render (request, 'visualizar_cadastro.html', ctx)
    
class DeletarCadastroView(LoginRequiredMixin, View):
    def post(self, request, id):
        cadastro = get_object_or_404(Cadastros, id=id, usuario=request.user)
        cadastro.delete()
        return redirect('aplicacao:home_cadastros')
    
class EditarCadastroView(LoginRequiredMixin, View):

    def get(self, request, id):

        cadastro_obj = get_object_or_404(Cadastros, id=id, usuario=request.user)
        return render(request, 'editar.html', {'cadastro': cadastro_obj})

    def post(self, request, id):

        cadastro = get_object_or_404(Cadastros, id=id, usuario=request.user)

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

        return redirect('aplicacao:visualizar_cadastros', id=cadastro.id)

class GerenciarSkillsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'gerenciar_skills.html')
    
    def post(self, request):
        skillSelecionada = request.POST.get('nameSelectBox')

        if skillSelecionada:
            cadastros_filtrados = Cadastros.objects.filter(usuario = request.user, **{skillSelecionada: True})
        else:
            cadastros_filtrados = Cadastros.objects.filter(usuario = request.user)

        return render(request, 'gerenciar_skills.html', {'cadastrosFiltrados': cadastros_filtrados})
    
class GerenciarPastasView(LoginRequiredMixin, View):
    def get(self, request):
        pastas = Pasta.objects.filter(usuario = request.user)
        cadastros = Cadastros.objects.filter(usuario = request.user)
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

class CriarPastaView(LoginRequiredMixin, View):
    def get(self, request):
        cadastros = Cadastros.objects.filter(usuario = request.user)  # Todos os cadastros disponíveis
        return render(request, 'criar_pasta.html', {'cadastros': cadastros})

    def post(self, request):
        nome_pasta = request.POST.get('nomePasta')
        cadastros_selecionados = request.POST.getlist('cadastros')

        if nome_pasta:
            pasta = Pasta.objects.create(nome=nome_pasta, usuario=request.user)
            if cadastros_selecionados:
                pasta.cadastros.set(Cadastros.objects.filter(id__in = cadastros_selecionados, usuario = request.user))
            pasta.save()

        return redirect('aplicacao:gerenciar_pastas')

class DetalhesPastaView(LoginRequiredMixin, View):
    def get(self, request, id):
        pasta = get_object_or_404(Pasta, id=id, usuario=request.user)
        # Passando as mulheres associadas à pasta
        ctx = {
            'pasta': pasta,
        }
        return render(request, 'detalhes_pasta.html', ctx)
    
class DeletarPastaView(LoginRequiredMixin, View):
    def post(self, request, id):
        pasta = get_object_or_404(Pasta, id=id, usuario=request.user)
        pasta.delete()  # Deleta o objeto Pasta
        return redirect('aplicacao:gerenciar_pastas')

class HomeBrinquedosView(LoginRequiredMixin, View):
    def get(self, request):
        
        brinquedo = Brinquedo.objects.filter(usuario = request.user).order_by('-id')

        ctx = { 'todos_brinquedos': brinquedo, }

        return render(request, 'home_brinquedos.html', ctx)

class RegistrarBrinquedoView(LoginRequiredMixin, View):
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
        brinquedo.usuario = request.user
        

        brinquedo.save()

        messages.success(request, 'Brinquedo adicionado com sucesso!')
        return redirect('aplicacao:home_brinquedos')
    
class VisualizarBrinquedoView(LoginRequiredMixin, View):
    def get(self, request, id):
        ctx = {'brinquedo':Brinquedo.objects.filter(id=id, usuario=request.user)}

        return render (request, 'visualizar_brinquedo.html', ctx)
    
class DeletarBrinquedoView(LoginRequiredMixin, View):
    def get(self, request, id):
        brinquedo = get_object_or_404(Brinquedo, id=id, usuario=request.user)

        return render(request, 'deletar_brinquedo.html', brinquedo)

    def post(self, request, id):
        brinquedo = get_object_or_404(Brinquedo, id=id, usuario = request.user)
        brinquedo.delete()
        messages.success(request, 'Brinquedo deletado com sucesso!')
        return redirect('aplicacao:home_brinquedos')
    
class EditarBrinquedoView(LoginRequiredMixin, View):

    def get(self, request, id):

        brinquedo = get_object_or_404(Brinquedo, id=id, usuario=request.user)
        return render(request, 'editar_brinquedo.html', {'brinquedo': brinquedo})

    def post(self, request, id):

        brinquedo = get_object_or_404(Brinquedo, id=id, usuario=request.user)
        
        brinquedo.nome = request.POST.get('nameFormBrinquedoNomeEdit')
        brinquedo.categoria = request.POST.get('nameFormBrinquedoCategoriaEdit')
        brinquedo.materiais = request.POST.get('nameFormBrinquedoMateriaisEdit')
        brinquedo.tematica = request.POST.get('nameFormBrinquedoTematicaEdit')
        brinquedo.quantidade = request.POST.get('nameFormBrinquedoQuantidadeEdit')
        brinquedo.usuario = request.user

        brinquedo.save()

        messages.success(request, 'Brinquedo editado com sucesso!')
        return redirect('aplicacao:home_brinquedos')
    