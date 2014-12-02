from django.db import models
from django.contrib.auth.models import User
from django.db import transaction, connection
# Create your models here.


class User(models.Model):
        username = models.CharField(max_length = 20)
        email = models.CharField(max_length = 50)
        password = models.CharField(max_length = 20)
        def __str__(self):
                return self.username

class Restaurant(models.Model):   
	name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 100)
	#typeR = models.CharField(max_length = 20)
	#models.ForeignKey(Type, null=True)
	phoneNumber = models.CharField(max_length = 11)
	picture = models.CharField(max_length = 120)
	def __str__(self):
		return self.name
	
class Type(models.Model):
	typeR = models.CharField(max_length = 20)
	restaurant = models.ForeignKey(Restaurant, null=True)
        

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

def my_custom_sql():
	print('hi')
	from django.db import connection, transaction
	cursor = connection.cursor()
	print('before execute')
	cursor.execute("UPDATE food SET averageRating = 1 WHERE food_id = %s", 2)
	print('after execute')
	transaction.commit_unless_managed()
	
#SQL Code Example:
'''
CREATE TABLE "users" (
	username varchar(20) NOT NULL,
	email varchar(50) NOT NULL,
	passowrd varchar(20) NOT NULL
);

CREATE TABLE "foods"(
	restaurant varchar(30) FOREIGN KEY REFERENCES Restaurant(name),
	name varchar(20) NOT NULL,
	price varchar(10) NOT NULL,
	averageRating int DEFAULT 0
)
'''