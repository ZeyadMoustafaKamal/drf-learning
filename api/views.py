from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerialzer

@api_view(['GET'])
def index(request):
    data = {}
    product = Product.objects.all().order_by('?').first()
    if product:
        data = ProductSerialzer(product).data
    return Response(data)
