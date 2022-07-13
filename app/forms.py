from django import forms
from .models import Contacto, Producto, Animal
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):
    
    
    class Meta:
        model = Contacto
        #fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields ='__all__'
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        #fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields ='__all__'
        
class AnimalForm(forms.ModelForm):
    
    class Meta:
        model = Animal
        #fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields ='__all__'

class CustomUserCreationForm(UserCreationForm):
    pass