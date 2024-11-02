from django.db import models
from .user import User


class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.FloatField()
	description = models.CharField(max_length=255)
	stock = models.IntegerField()
	seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
