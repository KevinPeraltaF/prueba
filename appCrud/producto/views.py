#Django file import
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import  HttpResponseRedirect
from django.db.models import ProtectedError

#Import my file
from .models import Producto
from .forms import ProductoForm

# Create your views here.


class ProductoListView(ListView):
    model = Producto
    template_name = "producto/producto_list.html"
    paginate_by = 4
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Listado de productos"
        context['entidad'] = "productos"
        return context

class ProductoCreateView(SuccessMessageMixin,CreateView):
    model = Producto
    form_class=ProductoForm
    success_url = reverse_lazy('producto_list')
    success_message = 'Registro Guardado Exitosamente!'
    template_name = "producto/producto_create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de registro"
        return context

class ProductoUpdateView(SuccessMessageMixin,UpdateView):
    model = Producto
    form_class=ProductoForm
    success_url = reverse_lazy('producto_list')
    success_message = 'Registro Editado Exitosamente!'
    template_name = "producto/producto_update.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de modificar"
        return context
    

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/producto_detail.html"


class ProductoDeleteView(SuccessMessageMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')
    success_message = 'Registro Eliminado Exitosamente!'
    template_name = "producto/producto_delete.html"
    
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

