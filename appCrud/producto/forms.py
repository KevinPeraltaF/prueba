from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                # Le añadimos clases CSS a los inputs
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
