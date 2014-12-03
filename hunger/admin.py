from django.contrib import admin
from hunger.models import Food, Restaurant, SocialNetworking
from hunger.models import  Nutrition, FoodRating

class FoodInline(admin.TabularInline):
    model = Food
    extra = 3
    
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [ (None,  {'fields':['name']}),
                  ('Information', {'fields':('location','phoneNumber','picture', 'faceBookLikeURL', 'hasTwitter', 'twitterHandle', 'totalLike', 'totalTweet')}),
                ]
    inlines =[FoodInline]
    list_display = ('name','phoneNumber','picture','location', 'faceBookLikeURL', 'hasTwitter', 'twitterHandle', 'totalLike', 'totalTweet')
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
    
class SocialStatsAdmin(admin.ModelAdmin):
  fieldSets = fieldsets = [ (None, {'fields':['id']}),
                  ('Info', {'fields':('numberOfTweets','likedOnOurSite','user','restaurant',)}),
                  ]
  list_display =('numberOfTweets','likedOnOurSite','user','restaurant')
  search_fields =['id']  

class FoodAdmin(admin.ModelAdmin):
    fieldsets = [ (None, {'fields':['name']}),
                  ('Info', {'fields':('restaurant','price','averageRating')}),
                  ]
    list_display =('name', 'restaurant', 'price', 'averageRating')
    search_fields =['name']
# Register your models here.
admin.site.register(Food, FoodAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(SocialNetworking,SocialNetworkingAdmin)
admin.site.register(Nutrition,NutritionAdmin)
admin.site.register(FoodRating)
