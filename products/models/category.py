from lib2to3.pytree import Base
from django.db import models

from core.models.base_model import BaseModel

class Category(BaseModel):
    
    name= models.CharField(max_length=250,null=False,blank=False)
