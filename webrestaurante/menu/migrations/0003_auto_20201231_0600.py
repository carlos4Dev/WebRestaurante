# Generated by Django 2.2.3 on 2020-12-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20201230_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='categoria_id',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='nombre',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='nombre',
            field=models.ManyToManyField(related_name='get_pedidos', to='menu.Plato', verbose_name='Platos'),
        ),
    ]
