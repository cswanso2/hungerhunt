from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
	type = models.CharField(max_length = 20)


class User(models.Model):
        username = models.CharField(max_length = 20)
        email = models.CharField(max_length = 50)
        password = models.CharField(max_length = 20)
        def __str__(self):
                return self.username

class Restaurant(models.Model):   
	name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 100)
	type = models.ForeignKey(Type, null=True)
	phoneNumber = models.CharField(max_length = 11)
	picture = models.CharField(max_length = 120)
	def __str__(self):
		return self.name
	
class Food(models.Model):
        restaurant = models.ForeignKey(Restaurant)
        name = models.CharField(max_length = 20)
        price = models.CharField(max_length = 10)
        averageRating = models.IntegerField(default = 0)
        def __str__(self):
                return self.name


class SocialNetworking(models.Model):
        name = models.CharField(max_length = 20)
        email = models.CharField(max_length = 50)
        password = models.CharField(max_length = 20)
        def my_email(self):
                return self.email
        def social_networking_name(self):
                return self.name

# one to One relationship with food, so this is a merge with relationship table	
class Nutrition(models.Model):
	food = models.OneToOneField(Food)
	fat = models.IntegerField()
	protein = models.IntegerField()
	sugar = models.IntegerField()
	carbs = models.IntegerField()
	calories = models.IntegerField()

	
# relationship Has_Eaten
class FoodRating(models.Model):
	user = models.ForeignKey(User)
	food = models.ForeignKey(Food)
	rating = models.IntegerField(default=0)


class Share(models.Model):
        foodName = models.ForeignKey(Food)
        socialName = models.ForeignKey(SocialNetworking)
