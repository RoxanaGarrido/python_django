
from tutorial.models import Book, Author, Publisher
from random import randint
from django.db.models import Avg, Sum, Min, Max, Count

def main():
    # Crear un autor con cada nombre
    # La edad aleatoria
    nombres = ['Ana','Miguel','Nuria','Raul','Sofia']

    for n in nombres:
        autor = Author(name=n, age=randint(18,65))
        autor.save()

def consultasAgregacion():
    # Precio medio de todos los libros:
    d = Book.objects.all().aggregate(precio_medio=Avg('price'))
    print('Precio medio de los libros: ', d)

    d2 = Book.objects.all().aggregate(Avg('price'))
    print('Precio medio de los libros: ', d2)

    # Suma de precios de los libros de cobol
    d3 = Book.objects.filter(name__contains='cobol').aggregate(Sum('price'))
    print('Suma del precio de los libros de cobol:', d3)


def consultasGrupos():
    # Consultas con annotate, opera a nivel de grupos
    # Hace grupos y por cada grupo aplica una funcion
    # de agregado.
    L = Publisher.objects.annotate(num_books=Count('book'))
    print('Num libros por editor:')
    for obj in L:
        print(obj.name, 'num_libros: ', obj.num_books)

