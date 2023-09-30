# Generated by Django 4.2.4 on 2023-09-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0002_remove_ubicación_producto_id'),
        ('produccion', '0002_alter_produto_tipo_ingrediente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria_id',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='uso',
        ),
        migrations.AddField(
            model_name='produto',
            name='almacen_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='logistica.almacen'),
        ),
        migrations.AddField(
            model_name='produto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
