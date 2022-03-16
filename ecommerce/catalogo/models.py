from django.db import models




class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self) :
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)    
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos')
    descricao = models.TextField()    
    
    def __str__(self) :
        return self.nome
