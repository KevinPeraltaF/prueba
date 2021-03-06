# Generated by Django 3.2.11 on 2022-01-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0002_producto_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha de venta')),
                ('cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
