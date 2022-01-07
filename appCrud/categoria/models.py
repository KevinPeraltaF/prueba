from django.db import models

# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria."""

    # TODO: Define fields here
    categoria  = models.CharField("Categoria", max_length=100, unique=True, help_text="Ingrese una categoría")

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.categoria
    

  
