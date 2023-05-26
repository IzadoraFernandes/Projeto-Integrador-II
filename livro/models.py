from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    descricao_categoria = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    
    def __str__(self) -> str:
        return self.nome_categoria
    
class Livros(models.Model):
    nome_livro = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length= 30, blank= True, null=True)
    data_cadastro = models.DateField(default = date.today)
    quantidade = models.IntegerField()
    emprestado = models.BooleanField(default=False)
    descricao_livro = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    editora = models.CharField(max_length = 100)
    data_lancamento = models.DateField(default = date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) # se a categoria for apagada ele simplesmente ignora.

    
    class Meta:
        verbose_name = 'Livro' #para retirar os dois s.
        
    def __str__(self):
        return self.nome_livro
    
class Emprestimo(models.Model):
    
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    
    nome_emprestado_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True, related_name='emprestimo_usuario') #registro de usuários cadastrados no sistema.
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank = True, null = True) #para usuários não cadastrados no sistema
    data_devolucao = models.DateTimeField(blank= True, null=True)
    tempo_duracao = models.DateField(blank= True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"