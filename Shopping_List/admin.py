from django.contrib import admin
from .models import Grocery_list
from .models import Recipe

admin.site.register(Grocery_list)
admin.site.register(Recipe)

# Register your models here.
