from django.shortcuts import render

def index(request):
    return render(request,'CORE/index.html',{"saludo" : "Holaaaa"})
