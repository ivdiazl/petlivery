from django.urls import path, include
from .views import home, cotizacion, webService, productos, contacto, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset, animales, agregar_animal, listar_animales, modificar_animal, eliminar_animal
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('cotizacion/', cotizacion, name="cotizacion"),
    path('webService/', webService, name="webService"),
    path('productos/', productos, name="productos"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('animales/', animales, name="animales"),
    path('agregar-animal/', agregar_animal, name="agregar_animal"),
    path('listar-animales/', listar_animales, name="listar_animales"),
    path('modificar-animal/<id>/', modificar_animal, name="modificar_animal"),
    path('eliminar-animal/<id>/', eliminar_animal, name="eliminar_animal"),
]