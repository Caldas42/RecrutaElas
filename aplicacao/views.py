from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import cadastros , Comentario

class HomeView(View):
    def get (self, request):
        cadastro = cadastros.objects.all()

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

            Cadastro = cadastros(nome = nome, idade = idade, cpf = cpf, celular = celular, cep = cep, cidade = cidade, bairro = bairro, rua = rua, numero = numero, complemento = complemento)

            Cadastro.save()

            return redirect('aplicacao:home')

class VisualizarCadastroView(View):
    def get(self, request, id):
        # Pega o cadastro específico
        cadastro = get_object_or_404(cadastros, id=id)

        # Pega os comentários associados ao cadastro (colaborador)
        comentarios = Comentario.objects.filter(colaborador=cadastro)

        # Passa o cadastro e os comentários para o template
        ctx = {
            'cadastro': cadastro,
            'comentarios': comentarios,
        }

        return render(request, 'visualizar_cadastro.html', ctx)
    


def adicionar_comentario(request):
    if request.method == 'POST':
        # Pega o nome do colaborador selecionado e o texto do comentário
        colaborador_nome = request.POST.get('colaborador')
        texto = request.POST.get('texto')

        # Obtém o colaborador pelo nome
        colaborador = cadastros.objects.get(nome=colaborador_nome)  # Certifique-se de usar cadastros ou Colaborador

        # Cria o comentário associado ao colaborador
        comentario = Comentario.objects.create(colaborador=colaborador, texto=texto)
        comentario.save()

        # Redireciona para a página de visualização de cadastros ou outra página desejada
        return redirect('aplicacao:home')  # Modifique conforme necessário
    else:
        # Exibe os colaboradores disponíveis no formulário para o usuário escolher
        colaboradores = cadastros.objects.all()  # Corrigido para cadastros
        return render(request, 'adicionar_comentario.html', {'colaboradores': colaboradores})