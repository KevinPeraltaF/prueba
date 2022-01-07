#Django
from django.urls import path

from producto import views as key


urlpatterns = [

    path('producto/', key.ProductoListView.as_view(), name="producto_list") ,
    path('producto/crear/', key.ProductoCreateView.as_view(), name="producto_create") ,
    path('producto/Editar/<int:pk>', key.ProductoUpdateView.as_view(), name="producto_update"),
    path('producto/Eliminar/<int:pk>', key.ProductoDeleteView.as_view(), name="producto_delete"),
    path('producto/Detalle/<int:pk>', key.ProductoDetailView.as_view(), name="producto_detail") 
  
]

