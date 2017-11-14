from django.db import models

# Create your models here.
class Grocery_list(models.Model):
    grocery_text=models.CharField(max_length=200)

class grocery_item(models.Model):
    grocery=models.ForeignKey(Grocery_list,on_delete=models.CASCADE)
    grocery_text=models.CharField(max_length=200)
    numofIngredient=models.IntegerField(default=0)
