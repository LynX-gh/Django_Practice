from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, 'Nickname must be greater than 1 character')]
        )

    def __str__(self):
        """Return name when print is called"""
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, 'Nickname must be greater than 1 character')]
        )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=200)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """Return nickname when print is called"""
        return self.nickname
