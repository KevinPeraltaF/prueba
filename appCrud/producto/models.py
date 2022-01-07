from django.db import models

from categoria.models import Categoria
from marca.models import Marca

# Create your models here.
class Producto(models.Model):

    producto = models.CharField(("Producto"), max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, verbose_name=("Categoria"), on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, verbose_name=("Marca"), on_delete=models.PROTECT)
    stock = models.IntegerField("Stock")
    precio = models.DecimalField(("Precio"), default="0", max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.producto
    
  

 