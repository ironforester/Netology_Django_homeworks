from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
import datetime

from django.http import HttpResponse

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['products__title', 'products__description']

@api_view(['GET'])
def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return Response(msg)