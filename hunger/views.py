from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from hunger.models import Restaurant, Food, Nutrition
from forms import UserForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
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

# Create your views here.
def hunger(request):
	restaurants = list(Restaurant.objects.all())
	restaurantFoodNutrition = {}
	for restaurant in restaurants:
		foods = list(Food.objects.filter(restaurant__id=restaurant.id))
		foodNutrition = {}
		for food in foods:
			nutrition = Nutrition.objects.get(food_id=food.id)
			foodNutrition[food] = nutrition
		restaurantFoodNutrition[restaurant] = foodNutrition
	return render_to_response('index.html', {'restaurantFoodNutrition': restaurantFoodNutrition})
