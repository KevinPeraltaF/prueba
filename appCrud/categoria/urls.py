#Django
from django.urls import path

from categoria import views as key


urlpatterns = [

    path('categoria/', key.CategoriaListView.as_view(), name="categoria_list") ,
    path('categoria/crear/', key.CategoriaCreateView.as_view(), name="categoria_create") ,
    path('categoria/Editar/<int:pk>', key.CategoriaUpdateView.as_view(), name="categoria_update"),
    path('categoria/Eliminar/<int:pk>', key.CategoriaDeleteView.as_view(), name="categoria_delete"),
    path('categoria/Detalle/<int:pk>', key.CategoriaDetailView.as_view(), name="categoria_detail") 
  
]

