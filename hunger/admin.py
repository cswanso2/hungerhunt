from django.contrib import admin
from hunger.models import User, Food, Restaurant, SocialNetworking
from hunger.models import  Nutrition, FoodRating, Share

class UserAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['username']}),
                  ('Log In', {'fields':('email','password')}),
                ]
    list_display = ('username','email')
    search_fields =['username']

class FoodInline(admin.TabularInline):
    model = Food
    extra = 3
    
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['name']}),
                  ('Information', {'fields':('location','phoneNumber','picture')}),
                ]
    inlines =[FoodInline]
    list_display = ('name','phoneNumber','picture','location')
    search_fields =['name']

class SocialNetworkingAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['name']}),
                  ('Log In', {'fields':('email','password')}),
                ]
    list_display = ('name','email','password')
    search_fields =['name']

################Nutrition maybe#############33
class NutritionAdmin(admin.ModelAdmin):
    fieldsets = [ (None, {'fields':['food']}),
                  ('Info', {'fields':('fat','protein','sugar','carbs','calories')}),
                  ]
    list_display =('food','fat','protein','sugar','carbs','calories')
    search_fields =['food']
    
class FoodAdmin(admin.ModelAdmin):
    fieldsets = [ (None, {'fields':['name']}),
                  ('Info', {'fields':('restaurant','price','averageRating')}),
                  ]
    list_display =('name','restaurant', 'price', 'averageRating')
    search_fields =['name']
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(SocialNetworking,SocialNetworkingAdmin)
admin.site.register(Nutrition,NutritionAdmin)
admin.site.register(FoodRating)
admin.site.register(Share)
