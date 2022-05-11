from rest_framework import serializers

from main.models import Shop, Goods


class ShopListSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'


class GoodsListSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'


