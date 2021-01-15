from .models import Pedidos, Plato
from rest_framework import serializers

class PedidosSerializer(serializers.ModelSerializer):
    nombre = serializers.PrimaryKeyRelatedField(queryset=Plato.objects.all(),many = True)
    status = serializers.ChoiceField(choices=Pedidos.STATUS_CHOICES)

    class Meta:
        model = Pedidos
        fields = ('pedido_id','cliente','nombre','status')

