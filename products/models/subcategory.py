from django.db import models
from core.models.base_model import BaseModel

from products.models.category import Category

class SubCategory(BaseModel):

    name = models.CharField(max_length=250,null=False,blank=False)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)