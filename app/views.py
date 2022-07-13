from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Animal
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, AnimalForm
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def home(request):
    return render(request, 'app/home.html')

def cotizacion(request):
    return render(request, 'app/cotizacion.html')

def webService(request):
    return render(request, 'app/webService.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html',data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "contacto guardado"
        else:
            data["form"]= formulario
    
    return render(request, 'app/contacto.html',data)

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html',data)

def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html',data)

def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto,id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html',data)

def eliminar_producto(request, id):
    
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)


def animales(request):
    animales = Animal.objects.all()
    data = {
        'animales': animales
    }
    return render(request, 'app/animales.html',data)

def agregar_animal(request):
    data = {
        'form': AnimalForm()
    }
    
    if request.method == 'POST':
        formulario = AnimalForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/animal/agregar.html',data)

def listar_animales(request):
    animales = Animal.objects.all()
    data = {
        'animales': animales
    }
    return render(request, 'app/animal/listar.html',data)

def modificar_animal(request, id):
    
    animal = get_object_or_404(Animal,id=id)
    data = {
        'form': AnimalForm(instance=animal)
    }
    
    if request.method == 'POST':
        formulario = AnimalForm(data=request.POST, instance=animal, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_animales")
        data["form"] = formulario
    
    return render(request, 'app/animal/modificar.html',data)

def eliminar_animal(request, id):
    
    animal = get_object_or_404(Animal,id=id)
    animal.delete()
    return redirect(to="listar_animales")
