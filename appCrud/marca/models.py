from django.db import models

# Create your models here.

class Marca(models.Model):
    """Model definition for Marca."""

    # TODO: Define fields here
    marca  = models.CharField("Marca", max_length=100, unique=True, help_text="Ingrese una Marca")

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
    def __str__(self):
        return self.marca
        
    

  
