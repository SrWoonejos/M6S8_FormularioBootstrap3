# Generated by Django 5.1.4 on 2025-01-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre'),
        ),
    ]
