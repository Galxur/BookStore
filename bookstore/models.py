from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{str(self.discount)} | {self.description}'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    in_stock = models.BooleanField(default=False)
    discount = models.ManyToManyField(Discount, blank=True)

    def __str__(self):
        return self.title

