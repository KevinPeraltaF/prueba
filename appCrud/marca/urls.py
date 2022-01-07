#Django
from django.urls import path

from marca import views as key


urlpatterns = [

    path('marca/', key.MarcaListView.as_view(), name="marca_list") ,
    path('marca/crear/', key.MarcaCreateView.as_view(), name="marca_create") ,
    path('marca/Editar/<int:pk>', key.MarcaUpdateView.as_view(), name="marca_update"),
    path('marca/Eliminar/<int:pk>', key.MarcaDeleteView.as_view(), name="marca_delete"),
    path('marca/Detalle/<int:pk>', key.MarcaDetailView.as_view(), name="marca_detail") 
  
]

