from django.db import models

# Create your models here.
AMOUNTS = (
    ('.125','1/8')
    ('.25','1/4')
    ('.5','1/2')
    ('.75','3/4')
    ('1.00','1')
    ('1.25','1 1/4')
    ('1.50','1 1/2')
    ('1.75','1 3/4')
    ('2', '2')
    ('2.25','2 1/4')
    ('2.50','2 1/2')
    ('2.75'.'2 3/4')
    ('3.00','3')
    ('4.00','4')
    ('5.00','5')
    ('6.00','6')
    ('7.00','7')
    ('8.00','8')
    ('9.00','9')
    ('10.00','10')
)

MEASURES = (
    ('t','Teaspoon')
    ('T','Tablespoon')
    ('cup','Cup')
    ('piece','Piece(s)')
)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 50)

class Ingredients(models.Model):
    recipename = models.ForeignKey(Recipe_Name)
    ingredient_amt = models.FloadField(max_length = 5,choices = AMOUNTS)
    ingredient_meas = models.CharField(max_length = 5, choices = MEASURES)
    ingredient_name = models.TextField(max_length = 50)

class Notes(models.Model):
    notes = models.TextField()
