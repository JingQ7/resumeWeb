from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    context = locals()
    tempalate = 'index.html'
    return render(request, tempalate, context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

def resume(request):
    context = locals()
    template = 'resume.html'
    return render(request, template, context)


