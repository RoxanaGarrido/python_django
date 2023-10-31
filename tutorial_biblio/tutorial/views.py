from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from tutorial.models import Fotografia, Book
import csv
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from tutorial.resources import BookResource

def index(request):
    return render(request, 'index.html')

def galeria(request):
    fotos = Fotografia.objects.all()
    context = {'fotos': fotos}
    return render(request, 'galeria.html', context)

def librosxml(request):
    libros = Book.objects.all()
    context={'libros':libros}

    return render(request, 'libros.xml', context, content_type='text/xml')

def libroscsv(request):
    L = Book.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=libros.csv'
    writer = csv.writer(response)

    encabezados = Book.get_cabeceras()
    writer.writerow(encabezados)
    for libro in L:
        fila = libro.to_list()
        writer.writerow(fila)
    return response

def librospdf(request):
    L = Book.objects.all()
    tabla_libros = [libro.to_list() for libro in L]
    tabla_libros.insert(0, Book.get_cabeceras())

    response = HttpResponse(content_type='application/pdf')
    pdf = canvas.Canvas(response, pagesize=landscape(A4))

    # Generar el contenido del PDF

    pdf.drawString(50,550, 'Listado de libros')
    tabla_pdf = Table(tabla_libros)

    # establecer el tamaño de la tabla
    tabla_pdf.wrapOn(pdf, 600,400)

    # dibujarla
    tabla_pdf.drawOn(pdf, 50, 325)
    pdf.showPage()
    pdf.save()
    return response

def librosjson(request):
    book = BookResource()
    registros = book.export()
    response = HttpResponse(registros.json, content_type='application/json')

    response['Content-Disposition'] = 'attachment; filename="books.json"'
    return response
    