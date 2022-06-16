from django import forms
from .models import Contacto, Producto

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
        
