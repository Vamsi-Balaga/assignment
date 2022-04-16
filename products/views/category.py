from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.serializers.category import CategorySerializer

from core.enum.statusEnum import StatusEnum
from products.models import Category

from json import loads

@csrf_exempt
def getCategories(request):
    categories=Category.objects.filter(status=StatusEnum.active).values()

    return JsonResponse(
        CategorySerializer(categories,many=True).data,
        safe=False
    )

