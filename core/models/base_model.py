from django.db import models
from django.utils import timezone

from core.enum.statusEnum import StatusEnum

class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    status = models.IntegerField(choices=StatusEnum.choices,default=StatusEnum.active)
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True