from django import forms
from .models import Marca

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                # Le añadimos clases CSS a los inputs
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
