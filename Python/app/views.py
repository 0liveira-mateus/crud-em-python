from django.shortcuts import render
from app.forms import carrosForm
from django.shortcuts import redirect
from app.models import carros

# Create your views here.
def home(request):
    data = {}
    data['db']= carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = carrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = carrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = carros.objects.get(pk=pk)
    return render(request, 'view.html', data)