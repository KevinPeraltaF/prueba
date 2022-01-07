from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    
    class Meta:
        model = Venta
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                # Le añadimos clases CSS a los inputs
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['producto'].widget.attrs['onchange'] = "consultarPrecio(); consultarCosto();"
            self.fields['cantidad'].widget.attrs['onchange'] = "consultarCosto();"
