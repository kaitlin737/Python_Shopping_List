from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery_list
from .models import Recipe
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import GroceryForm
from .forms import RecipeForm
from django import forms
from django.shortcuts import redirect
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
            Grocery_list.owner = request.user
            Grocery_list.save()
            return redirect('grocerylist_detail',pk=Grocery_list.pk)
    else:
        form=GroceryForm()
    return render(request,'Shopping_List/grocerylist_edit.html',{'form':form})

def edit_list(request,pk):
    grocerylist=get_object_or_404(Grocery_list,pk=pk)
    if request.method == 'POST':
        form = GroceryForm(request.POST, instance=grocerylist)
        if form.is_valid():
            grocerylist = form.save(commit=False)
            grocerylist.created_date = timezone.now()
            grocerylist.save()
            return redirect('grocerylist_detail',pk=grocerylist.pk)
    else:
        form = GroceryForm(instance=grocerylist)
    return render(request,"Shopping_List/grocerylist_edit.html", {'form':form,'pk':grocerylist})

def grocerylist_detail(request,pk):
     #saved_lists=get_object_or_404(Grocery_list,pk=pk)
     #return render(request, 'Shopping_List/grocerylist_detail.html',{'saved_lists':saved_lists})
     #title  get_object_or_404(Grocery_list, pk=pk)
     #text = get_object_or_404(Grocery_list, pk=pk)
     #Grocery_list.title=Grocery_list.objects.get(pk=pk)
     Grocery_list=get_object_or_404(Grocery_list,pk=pk)
     Hi = "hey"
     return render(request, 'Shopping_List/grocerylist_detail.html',{'Grocery_list':Grocery_list})

def saved_grocery_lists(request):
    user = request.user
    saved_lists = Grocery_list.objects.filter(owner=user)
    #saved_lists = Grocery_list.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
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

def grocery_delete(request, pk):
    grocerylist = get_object_or_404(Grocery_list, pk=pk)
    if request.method == 'POST':
        grocerylist.delete()
        return redirect('saved_grocery_lists')
    return render(request,'Shopping_List/grocerylist_detail.html', {'grocerylist': grocerylist})

class GroceryListForm(forms.ModelForm):
    class Meta:
        model = Grocery_list
        fields = ("title","text" )
def bound_form(request, pk):
    dairy=[]
    baked=[]
    fruitVeg=[]
    meat=[]
    canned=[]

    deptDict ={'milk':dairy, 'cheese':dairy,'sour cream':dairy, 'bread':baked,'steak':meat,'peanutbutter':canned}
    grocerylist = get_object_or_404(Grocery_list, pk=pk)

    items = grocerylist.text.split()
    for item in items:
        deptDict[item.lower()].append(item)



    return render(request,'Shopping_List/grocerylist_detail.html', {'grocerylist': grocerylist,  'dairy':dairy})

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

def recipe_list(request):
        saved_recipe_list = Recipe.objects.all()
        return render(request, 'Shopping_List/recipe_list.html',{'saved_recipe_list':saved_recipe_list})

def recipe_bound_form(request, pk):
    recipelist = get_object_or_404(Recipe, pk=pk)
    return render(request,'Shopping_List/recipe_list.html', {'recipelist': recipelist})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            Recipe = form.save(commit=False)
            Recipe.owner = request.user
            Recipe.save()
            return redirect('recipe_detail',pk=Recipe.pk)
    else:
        form = RecipeForm()
    return render(request,'Shopping_List/recipe_edit.html',{'form':form})

def edit_recipe(request,pk):
    recipelist=get_object_or_404(Recipe,pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipelist)
        if form.is_valid():
            recipelist = form.save(commit=False)
            recipelist.save()
            return redirect('recipe_detail',pk=recipelist.pk)
    else:
        form = RecipeForm(instance=recipelist)
    return render(request,"Shopping_List/recipe_edit.html", {'form':form,'pk':recipelist})

def recipe_detail(request,pk):
     Recipe=get_object_or_404(Recipe,pk=pk)
     return render(request, 'Shopping_List/recipe_add.html',{'Recipe':Recipe})


def recipelist_edit(request,pk):
     recipelist = get_object_or_404(Recipe, pk=pk)
     if request.method == "POST":
         form = RecipeForm(request.POST, instance=recipelist)
         if form.is_valid():
             recipelist = form.save(commit=False)
             recipelist.save()
             return redirect('recipe_edit', pk=recipelist.pk)
     else:
         form = RecipeForm(instance=recipelist)
     return render(request, 'Shopping_List/recipe_edit.html', {'form': form})

def recipe_delete(request, pk):
     recipelist = get_object_or_404(Recipe, pk=pk)
     if request.method == 'POST':
         recipelist.delete()
         return redirect('saved_recipe_lists')
     return render(request,'Shopping_List/recipe_add.html', {'recipelist': recipelist})
