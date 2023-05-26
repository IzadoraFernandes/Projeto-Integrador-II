from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria

def home(request):
    if request.session.get('usuario'): 
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.all()  #filter(usuario = usuario) só exibir os livros dele mesmo
        total_livros = livros.count()
        return render(request, 'home.html', {'livros':livros,})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario')) # para só exibir as categorias que o proprio usuário criou e não de todos.
            print(categoria_livro)
            return render(request, 'ver_livro.html', {'livro': livro,})
        else:
            return HttpResponse('Esse livro não é seu')
    else:
        return redirect('/auth/login/?status=2')