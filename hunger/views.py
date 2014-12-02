from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from hunger.models import Restaurant, Food, Nutrition
from forms import UserForm, FoodNutritionForm
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
from django.db import connection, transaction

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
    print request.REQUEST
    action = request.REQUEST['id']
    type, id = action.split('_')
    food = Food.objects.raw("SELECT * FROM hunger_food WHERE id == {}".format(id))[0]
    print('test is {}'.format(food))
    if type == 'upvote':
	cursor = connection.cursor()
	cursor.execute('UPDATE hunger_food SET averageRating = averageRating+1 WHERE name = (%s)', [food.name])
	cursor.execute("COMMIT;")
	print('hello')
    else:
	cursor = connection.cursor()
	cursor.execute('UPDATE hunger_food SET averageRating = averageRating-1 WHERE name = (%s)', [food.name])
	cursor.execute("COMMIT;")
    food.save()
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
