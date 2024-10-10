from django.db import models

class Category(models.Model):

    category = models.CharField(max_length=255, blank=False, null=False)


class Type(models.Model):

    type = models.CharField(max_length=255, blank=False, null=False)

class Size(models.Model):

    size = models.CharField(max_length=255, blank=False, null=False)

class Products(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)