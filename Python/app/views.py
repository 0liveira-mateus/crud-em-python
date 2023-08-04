from django.shortcuts import render, redirect
from app.forms import carrosForm
from app.models import carros

# Create your views here.
def home(request):
    data = { }
    data['db'] = carros.objects.all()
    return render(request, 'index.html', data)

def formulario(request):
    data = {}
    data['forms'] = carrosForm
    return render(request, 'formulario.html', data)

def create(request):
    form = carrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

def view(request, pk):
    data = {}
    data['db'] = carros.objects.get(pk=pk)
    return render(request, 'view.html', data)
