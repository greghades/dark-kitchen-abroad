# Generated by Django 4.2.4 on 2023-09-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='codigo',
            field=models.CharField(max_length=50),
        ),
    ]