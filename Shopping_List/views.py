from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery_list
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import GroceryForm
from django import forms
from django.shortcuts import redirect
from .models import Recipe
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def Home(request):
    return render(request, 'Shopping_List/Home.html')

def grocery_new(request):
    if request.method == "POST":
        form=GroceryForm(request.POST)
        if form.is_valid():
            Grocery_list=form.save(commit=False)
            Grocery_list.created_date=timezone.now()
            Grocery_list.save()
            return redirect('grocerylist_detail',pk=Grocery_list.pk)
    else:
        form=GroceryForm()
    return render(request,'Shopping_List/grocerylist_edit.html',{'form':form})



def saved_grocery_lists(request):
    saved_lists = Grocery_list.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'Shopping_List/saved_grocery_lists.html', {'saved_lists':saved_lists})

def grocerylist_edit(request,pk):
    #title = get_object_or_404(Grocery_list, pk=pk)
    #text = get_object_or_404(Grocery_list, pk=pk)
    grocerylist = get_object_or_404(Grocery_list, pk=pk)
    #post=Grocery_list.objects.get(pk=pk)
    if request.method == "POST":
        form = GroceryForm(request.POST, instance=grocerylist)
        if form.is_valid():
            grocerylist = form.save(commit=False)
            grocerylist.created_date = timezone.now()
            grocerylist.save()
            return redirect('grocerylist_detail', pk=grocerylist.pk)
    else:
        form = GroceryForm(instance=grocerylist)
    return render(request, 'Shopping_List/grocerylist_edit.html', {'form': form})

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = Grocery_list
        fields = ("title","text" )
def bound_form(request, pk):
    grocerylist = get_object_or_404(Grocery_list, pk=pk)
    return render(request,'Shopping_List/grocerylist_detail.html', {'grocerylist': grocerylist})

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('Home')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
def recipelist():
    context = {

        'heading': 'List of Recipes',
        'title': 'Recipe List',
        'recipe': recipe
    }"""

def recipe_add (request, recipe_id=None):
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
            recipe.ingredient_amt = request.POST.get('ingredient_amt')
            recipe.ingredient_meas = request.POST.get('ingredient_meas')
            recipe.ingredient_name = request.POST.get('ingredient_name')
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
            return render(request, 'Python_Shopping_List/recipe_add.html', data)
        else:
            recipe.recipe_name = string(recipe.recipe_name)
            recipe.ingredient_amt = float(recipe.ingredient_amt)
            recipe.ingredient_meas = float(recipe.ingredient_meas)
            recipe.ingredient_name = float(recipe.ingredient_name)
            recipe.notes = string(recipe.notes)
            recipe.save()

            data['heading'] = 'Success'
            data['content'] = 'Recipe added successfully!'
            data['recipe'] = recipe

            return render(request, 'Python_Shopping_List/recipe_add.html', data)
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
            return render(request, 'Python_Shopping_List/recipe_add.html', data)
