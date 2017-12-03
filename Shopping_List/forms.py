from django import forms
from .models import Grocery_list
from .models import Recipe
from .models import Ingredients
from betterforms.multiform import MultiModelForm

class GroceryForm(forms.ModelForm):
    class Meta:
        model=Grocery_list
        fields=('title','text',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name',)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ('ingredient_amt', 'ingredient_meas','ingredient_name')

class RecipeMultiForm(MultiModelForm):
    form_classes = {
        'recipe':RecipeForm,
        'ingredients':IngredientForm,
   }
