from django.contrib import admin
from .models import Grocery_list
from .models import Recipe
from .models import Ingredients
from .models import Notes

admin.site.register(Grocery_list)
admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Notes)


# Register your models here.
