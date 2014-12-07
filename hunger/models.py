from django.db import models
from django.contrib.auth.models import User
from django.db import transaction, connection
from datetime import datetime
# Create your models here.


class Restaurant(models.Model):   
	name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 100)
	#typeR = models.CharField(max_length = 20)
	#models.ForeignKey(Type, null=True)
	faceBookLikeURL = models.URLField(default=False)
	hasTwitter = models.BooleanField()
	twitterHandle = models.CharField(max_length = 50)
	phoneNumber = models.CharField(max_length = 11)
	picture = models.CharField(max_length = 120)
	totalTweet = models.IntegerField(default=0)
	totalLike = models.IntegerField(default=0)
	facebookId = models.CharField(max_length=120,null=True)
	def __str__(self):
		return self.name

class FacebookUser(models.Model):
	user = models.ForeignKey(User)
	access_token = models.CharField(max_length=1000)
	facebook_id = models.BigIntegerField(default = 0)


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
	time = models.DateTimeField(auto_now=True, default=datetime.now())
	food = models.ForeignKey(Food)
	rating = models.IntegerField(default=0)	


class SocialStat(models.Model):
	tweet = models.BooleanField(default=False)
	likedOnOurSite = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now=True, default=datetime.now())
	user = models.ForeignKey(User)
	restaurant = models.ForeignKey(Restaurant)
	

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