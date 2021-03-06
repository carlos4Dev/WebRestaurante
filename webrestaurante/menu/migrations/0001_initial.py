# Generated by Django 2.2.3 on 2021-02-05 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Categoria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('plato_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Plato')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Número pedido')),
                ('cliente', models.CharField(max_length=100, verbose_name='Nombre cliente')),
                ('status', models.CharField(choices=[('PROCESO', 'En_proceso'), ('TERMINADO', 'Terminado'), ('PAGADO', 'Pagado')], default='PROCESO', max_length=10)),
                ('nombre', models.ManyToManyField(related_name='get_pedidos', to='menu.Plato', verbose_name='Platos')),
            ],
        ),
    ]
