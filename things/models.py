from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Thing(Model):
    name = models.CharField(
        max_length=30, 
        unique=True,
        blank=False,
    )
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveSmallIntegerField(blank=False, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    
