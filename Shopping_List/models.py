from django.db import models
from django.utils import timezone

# Create your models here.
class Grocery_list(models.Model):
    title = models.CharField(max_length=140, default = "Enter Title")
    text=models.TextField(default = " ")
    created_date=models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('auth.User',null=True, on_delete=models.CASCADE)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title



AMOUNTS = (
    ('.125','1/8'),
    ('.25','1/4'),
    ('.5','1/2'),
    ('.75','3/4'),
    ('1.00','1'),
    ('1.25','1 1/4'),
    ('1.50','1 1/2'),
    ('1.75','1 3/4'),
    ('2', '2'),
    ('2.25','2 1/4'),
    ('2.50','2 1/2'),
    ('2.75','2 3/4'),
    ('3.00','3'),
    ('4.00','4'),
    ('5.00','5'),
    ('6.00','6'),
    ('7.00','7'),
    ('8.00','8'),
    ('9.00','9'),
    ('10.00','10'),
)

MEASURES = (
    ('t','Teaspoon'),
    ('T','Tablespoon'),
    ('cup','Cup'),
    ('piece','Piece(s)'),
)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 50, default = "Enter Recipe Name")
    ingredients = models.TextField(default = "")
    notes = models.TextField(default = "")
    owner = models.ForeignKey('auth.User',null=True, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.recipe_name

    class Meta:
        ordering = ["recipe_name"]
