from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response

from main.models import Shop, Goods
from main.serializers import ShopListSerializers, GoodsListSerializers
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'shop': reverse('shop-list', request=request, format=format),
        'goods': reverse('goods-list', request=request, format=format)
    })

class ShopViewSet(viewsets.ModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopListSerializers


class GoodsViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = Goods.objects.all()
    serializer_class = GoodsListSerializers

class GoodsFilter(filters.FilterSet):

    class Meta:
        model = Goods
        fields = ['name']

