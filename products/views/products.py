from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.serializers.product import CreateProductSerializer
from core.enum.statusEnum import StatusEnum
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


from products.models import Products
from products.serializers.product import ProductSerializer


@csrf_exempt
@api_view(["GET"])
def getProductsByCategory(request,category_id):
    products=Products.objects.filter(
        status=StatusEnum.active,
        subcategory__category_id=category_id
        ).values()

    return JsonResponse(
        ProductSerializer(products,many=True).data,
        safe=False
    )


@csrf_exempt
@api_view(["GET"])
def getProductsBySubCategory(request,subcategory_id):
    products=Products.objects.filter(
        status=StatusEnum.active,
        subcategory_id=subcategory_id
        ).values()

    return JsonResponse(
        ProductSerializer(products,many=True).data,
        safe=False
    )

@csrf_exempt
@api_view(["POST"])
def createProduct(request):
    data = JSONParser().parse(request)
    serializer = CreateProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


