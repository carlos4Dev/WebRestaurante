# Generated by Django 2.2.3 on 2020-12-30 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Número pedido')),
                ('cliente', models.CharField(max_length=100, verbose_name='Nombre cliente')),
                ('status', models.CharField(choices=[{'PROCESO', 'En_proceso'}, {'ENTREGA', 'Entregado'}, {'PAGADO', 'Pagado'}], default='PROCESO', max_length=10)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Categoria', verbose_name='Categoria')),
                ('nombre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Plato', verbose_name='Plato')),
            ],
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
