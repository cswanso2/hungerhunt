from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from hunger.models import Restaurant, Food, Nutrition, FoodRating, SocialStat
from forms import UserForm, FoodNutritionForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
from django.db import connection, transaction
from datetime import datetime
from datetime import timedelta
from bisect import bisect
import json
import random
import time

@csrf_protect
@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = UserForm()
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response("register.html", c)

@csrf_protect
@ensure_csrf_cookie
def foodNutrition(request):
	if request.method == 'POST':
		form = FoodNutritionForm(request.POST)
		if form.is_valid():
			price = str(request.REQUEST['price'])
			rating = str(request.REQUEST['averageRating'])
			restaurant = str(request.REQUEST['restaurant'])
			food = str(request.REQUEST['name'])
			calories = int(request.REQUEST['calories'])
			fat = int(request.REQUEST['fat'])
			protein = int(request.REQUEST['protein'])
			carbs = int(request.REQUEST['carbs'])
			sugar = int(request.REQUEST['sugar'])
			query1 = 'INSERT INTO hunger_food (name, restaurant_id, price, averageRating) VALUES ((%s), (%s), (%s), (%s))'
			cursor = connection.cursor()
			cursor.execute(query1, [food, restaurant, price, rating])
			cursor.execute("SELECT id FROM hunger_food WHERE name = %s", [food])
			food_id = cursor.fetchone()[0]
			query2 = 'INSERT INTO hunger_nutrition (food_id, carbs, calories, fat, protein, sugar) VALUES ((%s), (%s), (%s), (%s), (%s), (%s))'
			cursor.execute(query2, [food_id, carbs, calories, fat, protein, sugar])
			return HttpResponseRedirect("/home/")
	else:
		form = FoodNutritionForm()
	c = {'form': form}
	c.update(csrf(request))
	return render_to_response("foodnutrition.html", c)

@ensure_csrf_cookie
def trends(request):
	user = request.user
	foodRatings = []
	mostPopular = []
	popularToday = []
	for foods in Food.objects.raw("SELECT * FROM hunger_food ORDER BY averageRating DESC LIMIT 5"):
		foodRatings.append(foods)
	for restaurant in Food.objects.raw("SELECT *, totalLike + totalTweet as total FROM hunger_restaurant ORDER BY total DESC LIMIT 5"):
		mostPopular.append(restaurant)

	#get today and tomorrows date 
	now = datetime.now().strftime("%Y-%m-%d")
	tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
	for ratingObject in FoodRating.objects.raw("SELECT * FROM hunger_foodrating WHERE time >= '{}' AND time <= '{}' ORDER BY rating DESC LIMIT 5".format(now, tomorrow)):
		popularToday.append(ratingObject)
	return render_to_response("trends.html", {'foodRatings': foodRatings, 'mostPopular':mostPopular, 'user':user, 'popularToday':popularToday})

def getShared(userList, otherList):
	userIt = 0
	otherIt = 0
	shared = 0
	while otherIt < len(otherList) and userIt < len(userList):
		if otherList[otherIt] == userList[userIt]:
			shared += 1
			userIt += 1
		elif otherList[otherIt] > userList[userIt]:
			userIt += 1
		else:
			otherIt += 1
	return shared

def getFood(otherList):
	seed = random.randint(0, len(otherList) - 1)
	foodId = otherList[seed]
	food = Food.objects.raw("SELECT * FROM hunger_food WHERE id = {}".format(str(foodId)))[0]
	return food

@csrf_exempt
def recommend(request):
	user = request.user
	foodRatings = []
	for rating in FoodRating.objects.raw("SELECT * FROM hunger_foodrating"):
		foodRatings.append(rating)
	userFoodRatings = {}
	for rating in foodRatings:
		tempUser = rating.user
		if tempUser.id in userFoodRatings:
			userFoodRatings[tempUser.id].append(rating.food.id)
		else:
			userFoodRatings[tempUser.id] = [rating.food.id]
	if user.id not in userFoodRatings:
		return HttpResponse(json.dumps({'success': False}), content_type='application/json')
	userList = sorted(userFoodRatings[user.id])
	maxShared = 0
	otherId = -1
	
	for userKey in userFoodRatings:
		if userKey != user.id and userKey in userFoodRatings:
			otherList = sorted(userFoodRatings[userKey])
			shared = getShared(userList, otherList)
			if(shared > maxShared):
				maxShared = shared
				otherId = userKey
	count = 5
	otherList = userFoodRatings[otherId]
	while count > 0:
		food = getFood(otherList)
		if food.id not in userList:
			restaurantName = food.restaurant.name
			foodName = food.name
			payload = {'success': True, 'restaurantName': restaurantName, 'foodName': foodName, 'foodId': food.id}
			return HttpResponse(json.dumps(payload), content_type='application/json')
		count -= 1
	food = getFood(otherList)
	restaurantName = food.restaurant.name
	foodName = food.name
	payload = {'success': True, 'restaurantName': restaurantName, 'foodName': foodName, 'foodId': food.id}
	return HttpResponse(json.dumps(payload), content_type='application/json')

@csrf_exempt
def delete(request):
    id = int(request.REQUEST['id'])
    query = 'SELECT * FROM hunger_food WHERE id == {}'.format(id)
    food = str(Food.objects.raw(query)[0])
    cursor = connection.cursor()
    cursor.execute('DELETE FROM hunger_food WHERE name = (%s)', [food])
    cursor.execute("COMMIT;")
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

@csrf_exempt	
def vote(request):
    user = request.user
    action = request.REQUEST['id']
    type, id = action.split('_')
    food = Food.objects.raw("SELECT * FROM hunger_food WHERE id == {}".format(id))[0]
    user = request.user
    cursor = connection.cursor()
    if type == 'upvote':
		cursor.execute('UPDATE hunger_food SET averageRating = averageRating+1 WHERE name = (%s);', [food.name])
    else:
		cursor.execute('UPDATE hunger_food SET averageRating = averageRating-1 WHERE name = (%s);', [food.name])
    try:
    	foodVote = FoodRating.objects.raw("SELECT * FROM hunger_foodrating WHERE user_id = {} AND food_id = {}".format(user.id, food.id))[0]
    except:
    	if type == 'upvote':
    		rating = FoodRating(rating=1, user_id=user.id, food_id=food.id, time=datetime.now())
    		rating.save()
    	else:
    		rating = FoodRating(rating=-1, user_id=user.id, food_id=food.id, time=datetime.now())
    		rating.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

@csrf_exempt
def socialNetworkingUpdate(request):
	user = request.user
	name = request.REQUEST['name']
	cursor = connection.cursor()
	updateType = request.REQUEST['type']
	restaurant = Restaurant.objects.filter(name__iexact=name)[0]
	name = restaurant.name
	timeString =datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	if updateType == 'tweet':
		cursor.execute("INSERT INTO hunger_socialstat (user_id, restaurant_id, likedOnOurSite, tweet, time) VALUES ({},{},{},{},'{}');".format(user.id, restaurant.id, 0, 1, timeString))
	else:
		cursor.execute("INSERT INTO hunger_socialstat (user_id, restaurant_id, likedOnOurSite, tweet, time) VALUES ({},{},{},{},'{}');".format(user.id, restaurant.id, 0, 1, timeString))
	if(updateType=='tweet'):
		cursor.execute('UPDATE hunger_restaurant SET totalTweet =  totalTweet + 1 WHERE id = {};'.format(str(restaurant.id)))
	else:
		cursor.execute('UPDATE hunger_restaurant SET totalLike =  totalLike + 1 WHERE id = {};'.format(str(restaurant.id)))
	payload = {'success': True}
	return HttpResponse(json.dumps(payload), content_type='application/json')

def hunger(request):
	restaurants = []
	for restaurant in Restaurant.objects.raw("SELECT * FROM hunger_restaurant"):
		restaurants.append(restaurant)
	restaurantFoodNutrition = {}
	user = request.user
	for restaurant in restaurants:
		foods = []
		query = "SELECT * FROM hunger_food WHERE restaurant_id == {}".format(restaurant.id)
		for food in Food.objects.raw(query):
			foods.append(food)
		foodNutrition = {}
		for food in foods:
			query = "SELECT * FROM hunger_nutrition WHERE food_id == {} LIMIT 1".format(food.id)

			nutrition = Nutrition.objects.raw(query)[0]
			foodNutrition[food] = nutrition
		restaurantFoodNutrition[restaurant] = foodNutrition
	return render_to_response('index.html', {'restaurantFoodNutrition': restaurantFoodNutrition, 'user': user})
