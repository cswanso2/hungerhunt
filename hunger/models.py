from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name

class Restaurant(models.Model):
	name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 100)
	phoneNumber = models.CharField(max_length = 30)
	type = models.ForeignKey(Type)
	picture = models.CharField(max_length = 120)
	def __str__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(max_length = 30)
	price = models.CharField(max_length = 10)
	restaurant = models.ForeignKey(Restaurant)
	def __str__(self):
		return self.name
	
class Nutrition(models.Model):
	food = models.OneToOneField(Food)
	fat = models.IntegerField()
	protein = models.IntegerField()
	sugar = models.IntegerField()
	carbs = models.IntegerField()
	calories = models.IntegerField()

class Rating(models.Model):
	user = models.ForeignKey(User)
	food = models.ForeignKey(Food)
	rating = models.IntegerField()
