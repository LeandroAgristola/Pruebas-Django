from django.shortcuts import render
from blog.models import Post, Categoria #importamos el servicio del models de la APP servicios para poder trabajar sobre la vista servicios

# Create your views here.


def blog(request):
    posts=Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})

#Creamos la funcion que vamos a utilizar para filtrar los post por categoria, devuelvo el id correspondiente a cada categoria
def categoria(request, categoria_id): 
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    #en el render nos tiene que motrar la categoria filtrada y luego los post de esa categoria filtradad
    return render(request,"blog/categoria.html", {'categoria': categoria,"posts": posts})
