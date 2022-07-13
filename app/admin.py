from django.contrib import admin
from .models import Marca, Producto, Contacto, Tipo_animal, Animal
# Register your models here.


admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Tipo_animal)
admin.site.register(Animal)