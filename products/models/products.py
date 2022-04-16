from products.models.subcategory import SubCategory
from core.models.base_model import BaseModel
from django.db import models

class Products(BaseModel):
    
    name= models.CharField(max_length=250,null=False,blank=False)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=False,blank=False)