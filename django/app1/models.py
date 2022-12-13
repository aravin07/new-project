from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=35)
    author = models.CharField(max_length=15)
    published_year = models.IntegerField(default=0)
    language = models.CharField(max_length=15)
    cost = models.IntegerField(default=0)

    class Meta:
        db_table = 'book'
        ordering = ['book_name', 'author']
        verbose_name_plural = "books"