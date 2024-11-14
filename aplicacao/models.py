from django.db import models

class cadastros(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField(default=0)
    cpf = models.CharField(max_length=14, default="")
    celular = models.CharField(max_length=15, default="")
    cep = models.CharField(max_length=9, default="")
    cidade = models.CharField(max_length=30, default="Cidade não informada")
    bairro = models.CharField(max_length=100, default="Bairro não informado")
    rua = models.CharField(max_length=150, default="Rua não informada")
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=50, default="Complemento não informado")

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(cadastros, on_delete=models.CASCADE, null=True, blank=True)  # Referencia ao modelo Cadastros, não ao campo 'nome'
    
    def __str__(self):
        return self.texto[:50]
