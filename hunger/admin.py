from django.contrib import admin

from hunger.models import Type, Restaurant, Food, Nutrition, Rating
# Register your models here.
admin.site.register(Type)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Nutrition)
admin.site.register(Rating)