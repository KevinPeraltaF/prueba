from django.db import models
from producto.models import Producto

# Create your models here.
class Venta(models.Model):

    fecha = models.DateField("Fecha de venta", auto_now=True, auto_now_add=False)
    cliente = models.CharField("Cliente", max_length=100)
    producto = models.ForeignKey(Producto, verbose_name=("Producto"), on_delete=models.PROTECT)
    cantidad = models.IntegerField(("Cantidad"))
    
    class Meta:
        verbose_name = ("Venta")
        verbose_name_plural = ("Ventas")

    def __str__(self):
        return self.name
    
    def subtotal(self):
        subtotal = self.cantidad * self.producto.precio
        return subtotal
    
    
    


   

