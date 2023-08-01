from django.forms import ModelForm
from app.models import carros

# Create the form class.
class carrosForm(ModelForm):
    class Meta:
        model = carros
        fields = ["Modelo", "Marca", "Ano"]
