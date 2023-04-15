from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64) # hashlib 256 cria sempre uma rest de 64 caracteres, independente na quantidade que o usuario digitar.
    
    def __str__(self) -> str:
        return self.nome