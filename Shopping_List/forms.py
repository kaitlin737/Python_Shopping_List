from django import forms
from .models import Grocery_list

class GroceryForm(forms.ModelForm):
    class Meta:
        model=Grocery_list
        fields=('title','text',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name',)
