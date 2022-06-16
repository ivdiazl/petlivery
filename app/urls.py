from django.urls import path
from .views import home, cotizacion, webService, productos, contacto, agregar_producto, listar_productos, modificar_producto, eliminar_producto

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
]