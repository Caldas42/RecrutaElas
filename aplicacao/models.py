from django.db import models

# Create your models here.

class Cadastros(models.Model):
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

    skillCostura = models.BooleanField(default=False)
    skillGerenciamento = models.BooleanField(default=False)
    skillPintura = models.BooleanField(default=False)

class Pasta(models.Model):
    nome = models.CharField(max_length=100)
    cadastros = models.ManyToManyField(Cadastros, related_name="pastas")

    def __str__(self):
        return self.nome

class Brinquedo(models.Model):
    nome = models.CharField(max_length= 100)
    categoria = models.CharField(max_length= 100)
    materiais = models.CharField(max_length=200)
    tematica = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    imagem = models.FileField(upload_to='uploads/', blank=True, null=True)