# Generated by Django 4.2.4 on 2023-09-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_remove_produto_categoria_id_remove_produto_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fecha_expiracion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
