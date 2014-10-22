from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from hunger.models import Restaurant, Food, Nutrition
from forms import UserForm, FoodNutritionForm
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt

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
			food = form.save()
			calories = form.cleaned_data['calories']
			fat = form.cleaned_data['fat']
			protein = form.cleaned_data['protein']
			carbs = form.cleaned_data['carbs']
			sugar = form.cleaned_data['sugar']
			nutrition = Nutrition(food=food,carbs = carbs,calories = calories,fat = fat,protein = protein,sugar = sugar)
			nutrition.save()
			return HttpResponseRedirect("/home/")
	else:
		form = FoodNutritionForm()
	c = {'form': form}
	c.update(csrf(request))
	return render_to_response("foodnutrition.html", c)


@csrf_exempt
def delete(request):    
    food = Food.objects.get(id = int(request.REQUEST['id']))
    food.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

@csrf_exempt	
def vote(request):    
    print request.REQUEST
    action = request.REQUEST['id']
    type, id = action.split('_')
    food = Food.objects.get(id = id)
    if type == 'upvote':
	food.averageRating += 1
    else:
	food.averageRating -= 1
    food.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

def hunger(request):
	restaurants = list(Restaurant.objects.all())
	restaurantFoodNutrition = {}
	user = request.user
	for restaurant in restaurants:
		foods = list(Food.objects.filter(restaurant__id=restaurant.id))
		foodNutrition = {}
		for food in foods:
			nutrition = Nutrition.objects.get(food_id=food.id)
			foodNutrition[food] = nutrition
		restaurantFoodNutrition[restaurant] = foodNutrition
	return render_to_response('index.html', {'restaurantFoodNutrition': restaurantFoodNutrition, 'user': user})
