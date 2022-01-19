from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=32)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=32)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=64)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=16, null=True)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    justification = models.CharField(max_length=300, null=True)
    year = models.IntegerField(null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=13)
    latitude = models.DecimalField(max_digits=17, decimal_places=13)
    area_hectares = models.DecimalField(max_digits=16, decimal_places=5, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name