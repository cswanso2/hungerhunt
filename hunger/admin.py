from django.contrib import admin
from hunger.models import User, Food, Restaurant, SocialNetworking
from hunger.models import  Nutrition, FoodRating, Share

class UserAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['username']}),
                  ('Log In', {'fields':('email','password')}),
                ]
    list_display = ('username','email','password')
    search_fields =['username']

class FoodInline(admin.TabularInline):
    model = Food
    extra = 3
    
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['name']}),
                  ('Information', {'fields':('location','phoneNumber','type')}),
                ]
    inlines =[FoodInline]
    list_display = ('name','phoneNumber','type','location')
    search_fields =['name']

class SocialNetworkingAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['name']}),
                  ('Log In', {'fields':('email','password')}),
                ]
    list_display = ('name','email','password')
    search_fields =['name']

################Nutrition maybe#############33


    
# Register your models here.
admin.site.register(User)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(SocialNetworking)
admin.site.register(Nutrition)
admin.site.register(FoodRating)
admin.site.register(Share)
