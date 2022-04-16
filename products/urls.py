from xml.etree.ElementInclude import include
from django.urls import path


from rest_framework import routers

# from products.views.category import CategoriesViewSet
  
# import everything from views
from .views import category,subcategory,products
# define the router
router = routers.DefaultRouter()
  

# router.register(r"categories", CategoriesViewSet)


urlpatterns = [
    path('getCategories', category.getCategories),
    path("getSubCategories/<int:category_id>",subcategory.getSubCategories),

    path("getProductsByCategory/<int:category_id>", products.getProductsByCategory),
    path("getProductsBySubCategory/<int:subcategory_id>", products.getProductsBySubCategory),
    path("createProduct",products.createProduct)
]