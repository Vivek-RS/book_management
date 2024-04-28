from django.db import models
from datetime import datetime
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name
class Author(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    author_name = models.CharField(max_length=100)
    d_o_b = models.DateField(default = datetime.today)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField(default=1234567890)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
