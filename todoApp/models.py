from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length = 150)
    price = models.ImageField()
    author = models.CharField(max_length = 150)
    class Mata:
        db_table = "todoApp_booklist"
         
