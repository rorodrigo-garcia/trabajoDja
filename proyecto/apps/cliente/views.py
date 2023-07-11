from django.shortcuts import render

def cliente(request):
    context = {"nombre": "nombre del cliente"}
    return render(request,'cliente.html',context)