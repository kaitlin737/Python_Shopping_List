from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery_list
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.
def index(request):
    text="<h1> Welcome to my app</h1>"
    return HttpResponse(text)
def grocerylist_new(request):
    form=GroceryForm()
    return render(request,'Shopping_List/grocerylist_edit.html',{'form':form})
def saved_grocery_lists(request):
    return render(request,'Shopping_List/saved_grocery_lists.html')

def grocery_detail(request,pk):
    return render(request, 'blog/post_detail.html')
def recipelist():
    context = {
        'heading': 'List of Recipes',
        'title': 'Recipe List'
    }

"""def addrecipe():
    context = {
        'heading': 'To Add A Recipe',
        'title': 'Add Recipe'
    }"""

def addrecipe(request, recipe_id=None):
    errors = []
    if request.method == 'POST':
        # handle data posted from the from
        if not request.POST.get('recipe_name', ''):
            errors.append('Enter Recipe Name.')
        if not request.POST.get('ingredient_amt', ''):
            errors.append('Enter Ingredient Amount')
        if not request.POST.get('ingredient_meas', ''):
            errors.append('Enter Ingredient Measure')
        if not request.POST.get('ingredient_name', ''):
            errors.append('Enter Ingredient Name')

        if recipe_id:
            recipe = recipe.objects.get(pk=recipe_id)
        else:
            recipe = Recipe()
        recipe.recipe_name = request.POST.get('recipe_name')
        final_ingredient == False
        while final_ingredient == False:
            ingredients.ingredient_amt = request.POST.get('ingredient_amt')
            ingredients.ingredient_meas = request.POST.get('ingredient_meas')
            ingredients.ingredient_name = request.POST.get('ingredient_name')
            z = input("Would you like to add another ingredient? Enter y or yes to continue.")
            if (not z == "y" or z == "yes"):
                final_ingredient == True
                break
        notes.notes = requiest.POST.get('Notes')
        data = {
            'errors': errors,
            'recipe': recipe,
            }
        if errors:
            data['heading'] = 'Add New Recipe'
            data['content'] = 'Fill in the following information:'
            return render(request, 'Python_Shopping_List/add_recipe.html', data)
        else:
            recipe.recipe_name = string(recipe.recipe_name)
            recipe.save()
            ingredients.ingredient_amt = float(ingredients.ingredient_amt)
            ingredients.ingredient_meas = float(ingredients.ingredient_meas)
            ingredients.ingredient_name = float(ingredients.ingredient_name)
            ingredients.save()
            notes.notes = string(notes.notes)
            notes.save()

            data['heading'] = 'Success'
            data['content'] = 'Recipe added successfully!'
            data['recipe'] = recipe
            data['ingredients'] = Ingredients
            data['notes'] = notes
            return render(request, 'Python_Shopping_List/add_recipe.html', data)
    else:
        if not recipe_id:
            # must be a get method to enter new grade info so render the form for user to enter
            # data
            data = {
                'heading': 'Add New Recipe',
                'content': 'Fill in the following information',
                'errors': errors,
            }
        else:
            # edit existing student
            #student = Student.objects.get(pk=student_id)
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            data = {
                'heading': 'Edit Recipe',
                'content': 'Update the following information',
                'errors': errors,
                'recipe': recipe,
            }
            return render(request, 'Python_Shopping_List/add_recipe.html', data)
