from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from products.models import SubCategory
from products.serializers.subcategory import SubCategorySerializer
from core.enum.statusEnum import StatusEnum




@csrf_exempt
def getSubCategories(request,category_id):
    sub_categories=SubCategory.objects.filter(
                                        status=StatusEnum.active,
                                        category_id=category_id
                                        ).values()

    return JsonResponse(
        SubCategorySerializer(sub_categories,many=True).data,
        safe=False
    )
