from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Food, Nutrition, Restaurant

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(label=("First Name"))
	last_name = forms.CharField(label=("Last Name"))
	
	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "password1", "password2")

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user
	

class FoodNutritionForm(forms.ModelForm):
	
    calories = forms.IntegerField()
    fat = forms.IntegerField()
    protein = forms.IntegerField()
    carbs = forms.IntegerField()
    sugar = forms.IntegerField()
    class Meta:
		model = Food
		fields = ['restaurant', 'name', 'price', 'averageRating']


		