from django import forms
from .models import Grocery_list
from .models import Recipe

class GroceryForm(forms.ModelForm):
    class Meta:
        model=Grocery_list
        fields=('title','text',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name',)

class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name','ingredient_amt','ingredient_meas','ingredient_name','notes')
