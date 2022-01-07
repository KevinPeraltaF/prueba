#Django file import
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import  HttpResponseRedirect
from django.db.models import ProtectedError
from django.http import HttpResponse
import json
from producto.models import Producto
#Import my file
from .models import Venta
from .forms import VentaForm

# Create your views here.



class VentaListView(ListView):
    model = Venta
    template_name = "venta/venta_list.html"
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Listado de ventas"
        context['entidad'] = "ventas"
 
        return context

from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)


class VentaCreateView(SuccessMessageMixin,CreateView):
    model = Venta
    form_class=VentaForm
    success_url = reverse_lazy('venta_list')
    success_message = 'Registro Guardado Exitosamente!'
    template_name = "venta/venta_create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de registro"
        return context

def ConsultarTarifa(request):

    if request.method == 'GET':

        producto = request.GET['producto']
        precio = Producto.objects.values().all().filter(pk=producto)
        precio_list = list(precio)
        print(precio_list)
        data = {
            'resultado': 'ok_select',
            'precio': precio_list
        }
        return HttpResponse(json.dumps(data, cls=DecimalEncoder), content_type="application/json")

class VentaUpdateView(SuccessMessageMixin,UpdateView):
    model = Venta
    form_class=VentaForm
    success_url = reverse_lazy('venta_list')
    success_message = 'Registro Editado Exitosamente!'
    template_name = "venta/venta_update.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de modificar"
        return context
    

class VentaDetailView(DetailView):
    model = Venta
    template_name = "venta/venta_detail.html"


class VentaDeleteView(SuccessMessageMixin,DeleteView):
    model = Venta
    success_url = reverse_lazy('venta_list')
    success_message = 'Registro Eliminado Exitosamente!'
    template_name = "venta/venta_delete.html"
    
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

