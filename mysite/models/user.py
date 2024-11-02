from django.db import models

class User(models.Model):
	TITLE_CHOICES = [
		('Mr', 'Mr'),
		('Mrs', 'Mrs'),
		('Miss', 'Miss'),
		('Dr', 'Dr'),
		('Prof', 'Prof'),
	]
	username = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	title = models.CharField(choices=TITLE_CHOICES, null=True)
	email = models.EmailField(max_length=50)
	address = models.CharField(max_length=255, null=True)
