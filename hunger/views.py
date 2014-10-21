from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from hunger.models import Restaurant, Food, Nutrition

# Create your views here.
def hunger(request):
	restaurants = list(Restaurant.objects.all())
	if request.method == 'POST':
		print "halsdfkjas;dfjasd;fj\n\n\n\n\n\n\n\n"
	else:
		print 'not ajax'
	return render_to_response('index.html')
	
def restaurant(request, name):
	#try: 
		restaurant = Restaurant.objects.get(name__iexact=name)
		foods = Food.objects.filter(restaurant__name=restaurant.name)
		foodNutrition = {}
		response = "<h1>" + restaurant.name + "</h1><table>"
		for food in foods:
			nutrition = Nutrition.objects.get(food_id=food.id)
			foodNutrition[food] = nutrition
			response += "<tr><td>" + food.name + "</td><td>" + food.price + "</td><td>" + str(nutrition.calories) + "</td></tr>"
		response += "</table>"
		return render_to_response('restaurant_list.html', {'restaurant': restaurant, 'foodNutrition': foodNutrition})
	#except:
	#	return HttpResponse("none")