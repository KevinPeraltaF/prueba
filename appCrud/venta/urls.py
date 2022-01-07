#Django
from django.urls import path

from venta import views as key


urlpatterns = [

    path('venta/', key.VentaListView.as_view(), name="venta_list") ,
    path('venta/crear/', key.VentaCreateView.as_view(), name="venta_create") ,
    path('venta/Editar/<int:pk>', key.VentaUpdateView.as_view(), name="venta_update"),
    path('venta/Eliminar/<int:pk>', key.VentaDeleteView.as_view(), name="venta_delete"),
    path('venta/Detalle/<int:pk>', key.VentaDetailView.as_view(), name="venta_detail"),
    path('venta/crear/consultar_tarifa', key.ConsultarTarifa, name='consultar_tarifa'),
  
]

