from django.db import models

class Membro(models.Model):
    sexos = (('F', 'Feminino'), ('M', 'Masculino'))
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=sexos)
    cargo = models.ForeignKey('Cargo', on_delete=models.DO_NOTHING)
    cricao = models.DateTimeField(auto_now_add=True)
    alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    descricao = models.CharField(max_length=255)
    cricao = models.DateTimeField(auto_now_add=True)
    alteracao = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.descricao
        

class Departamento(models.Model):
    descricao = models.CharField(max_length=255)
    cricao = models.DateTimeField(auto_now_add=True)
    alteracao = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.descricao


