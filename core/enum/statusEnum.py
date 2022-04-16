
from django.db.models import IntegerChoices

class StatusEnum(IntegerChoices):
    
    active=1,"Active"
    inactive=0,"Inactive"