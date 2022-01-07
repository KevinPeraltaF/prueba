#Django file import
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import  HttpResponseRedirect
from django.db.models import ProtectedError

#Import my file
from .models import Marca
from .forms import MarcaForm

# Create your views here.


class MarcaListView(ListView):
    model = Marca
    template_name = "marca/marca_list.html"
    paginate_by = 4
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Listado de marcas"
        context['entidad'] = "marcas"
        return context

class MarcaCreateView(SuccessMessageMixin,CreateView):
    model = Marca
    form_class=MarcaForm
    success_url = reverse_lazy('marca_list')
    success_message = 'Registro Guardado Exitosamente!'
    template_name = "marca/marca_create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de registro"
        return context

class MarcaUpdateView(SuccessMessageMixin,UpdateView):
    model = Marca
    form_class=MarcaForm
    success_url = reverse_lazy('marca_list')
    success_message = 'Registro Editado Exitosamente!'
    template_name = "marca/marca_update.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Formulario de modificar"
        return context
    

class MarcaDetailView(DetailView):
    model = Marca
    template_name = "marca/marca_detail.html"


class MarcaDeleteView(SuccessMessageMixin,DeleteView):
    model = Marca
    success_url = reverse_lazy('marca_list')
    success_message = 'Registro Eliminado Exitosamente!'
    template_name = "marca/marca_delete.html"
    
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

