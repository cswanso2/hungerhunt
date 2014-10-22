from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from hunger.models import Restaurant, Food, Nutrition
from forms import UserForm
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

@csrf_exempt
def delete(request):    
    food = Food.objects.get(id = int(request.REQUEST['id']))
    food.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')
	
# Create your views here.
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
