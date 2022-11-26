from django.db import models
from .base_model import BaseModel
from .identity import Identity

class Person(BaseModel):
    name = models.CharField(max_length=80)

    identity = models.OneToOneField(
        Identity,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name