from django.contrib.auth.models import AbstractUser
from .base_model import BaseModel
from django.core.validators import EmailValidator
from django.db import models

class Identity(AbstractUser, BaseModel):
    username = models.CharField(max_length=255, unique=True, validators=[EmailValidator()])
    class Meta:
        db_table = "identity"
        verbose_name = "identity"
        verbose_name_plural = "identities"

    def __str__(self):
        return self.email
