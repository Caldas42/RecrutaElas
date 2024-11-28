from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cadastros, Pasta, Brinquedo, Comentario


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

            imagem = request.FILES.get('formCadastroImagem')

            skillCostura = request.POST.get('nameSkillCostura') == 'on'
            skillGerenciamento = request.POST.get('nameSkillGerenciamento') == 'on'
            skillPintura = request.POST.get('nameSkillPintura') == 'on'
            skillDesign = request.POST.get('nameSkillDesign') == 'on'
            skillCriatividade = request.POST.get('nameSkillCriatividade') == 'on'
            skillAtendimento = request.POST.get('nameSkillAtendimento') == 'on'
            skillVendas = request.POST.get('nameSkillVendas') == 'on'
            skillLimpeza = request.POST.get('nameSkillLimpeza') == 'on'
            
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
                                 usuario=request.user, 
                                 imagem=imagem)

            cadastro.save()

            messages.success(request, 'Cadastro adicionado com sucesso!')

            return redirect('aplicacao:home_cadastros')

class VisualizarCadastroView(LoginRequiredMixin, View):
    def get (self, request, id):

        cadastro = get_object_or_404(Cadastros, id=id, usuario=request.user)  # Certifica-se que pertence ao usuário
        comentarios = Comentario.objects.filter(colaborador=cadastro)

        ctx = {
            'cadastro': cadastro,
            'comentarios': comentarios,
        }

        return render(request, 'visualizar_cadastro.html', ctx)
    
class DeletarCadastroView(LoginRequiredMixin, View):
    def post(self, request, id):

        cadastro = get_object_or_404(Cadastros, id=id, usuario=request.user)

        cadastro.delete()

        messages.success(request, 'Cadastro deletado com sucesso!')
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

        messages.success(request, 'Cadastro editado com sucesso!')

        return redirect('aplicacao:home_cadastros')

class GerenciarSkillsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'gerenciar_skills.html')
    
    def post(self, request):
        skillSelecionada = request.POST.get('nameSelectBox')

        if skillSelecionada:
            cadastros_filtrados = Cadastros.objects.filter(usuario=request.user, **{skillSelecionada: True})
        else:
            cadastros_filtrados = Cadastros.objects.filter(usuario=request.user)

        return render(request, 'gerenciar_skills.html', {
            'cadastrosFiltrados': cadastros_filtrados,
            'skillSelecionada': skillSelecionada,  # Passa a habilidade selecionada
        })
    
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

        # Pegando todos os cadastros associados à pasta
        cadastros_na_pasta = pasta.cadastros.all()

        # Pegando todos os cadastros que NÃO estão associados a esta pasta
        colaboradoras_nao_associadas = Cadastros.objects.filter(usuario=request.user).exclude(id__in=cadastros_na_pasta.values('id'))

        ctx = {
            'pasta': pasta,
            'colaboradoras_nao_associadas': colaboradoras_nao_associadas,
        }
        return render(request, 'detalhes_pasta.html', ctx)
    
class DeletarPastaView(LoginRequiredMixin, View):
    def get(self, request, id):
        pasta = get_object_or_404(Pasta, id=id, usuario=request.user)
        pasta.delete()  # Deleta o objeto Pasta
        messages.success(request, 'Pasta deletada com sucesso!')
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
        
        brinquedo = get_object_or_404(Brinquedo, id=id, usuario=request.user)
        ctx = {'brinquedo': brinquedo}

        return render (request, 'visualizar_brinquedo.html', ctx)
    
class DeletarBrinquedoView(LoginRequiredMixin, View):
    def get(self, request, id):
        brinquedo = get_object_or_404(Brinquedo, id=id, usuario=request.user)

        return render(request, 'deletar_brinquedo.html', {'brinquedo': brinquedo})

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
    
class AdicionarColaboradorasView(LoginRequiredMixin, View):
    def post(self, request, pasta_id):
        pasta = get_object_or_404(Pasta, id=pasta_id, usuario=request.user)
        
        # Obtendo os IDs das colaboradoras selecionadas
        cadastros_selecionados = request.POST.getlist('cadastros')

        # Adicionando as colaboradoras selecionadas à pasta
        if cadastros_selecionados:
            cadastros = Cadastros.objects.filter(id__in=cadastros_selecionados)
            pasta.cadastros.add(*cadastros)  # Adiciona as colaboradoras à pasta

        messages.success(request, 'Colaboradoras adicionadas à pasta com sucesso!')
        return redirect('aplicacao:detalhes_pasta', id=pasta.id)
    

def adicionar_comentario(request):
    if request.method == 'POST':
        # Pega o nome do colaborador selecionado e o texto do comentário
        colaborador_nome = request.POST.get('colaborador')
        texto = request.POST.get('texto')

        # Obtém o colaborador pelo nome
        colaborador = Cadastros.objects.get(nome=colaborador_nome)  # Certifique-se de usar cadastros ou Colaborador

        # Cria o comentário associado ao colaborador
        comentario = Comentario.objects.create(colaborador=colaborador, texto=texto)
        comentario.save()

        # Redireciona para a página de visualização de cadastros ou outra página desejada
        return redirect('aplicacao:home_cadastros')  # Modifique conforme necessário
    else:
        # Exibe os colaboradores disponíveis no formulário para o usuário escolher
        colaboradores = Cadastros.objects.all()  # Corrigido para cadastros
        return render(request, 'adicionar_comentario.html', {'colaboradores': colaboradores})