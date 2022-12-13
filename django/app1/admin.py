from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "book_name", "author", "published_year", "language", "cost")
    search_fields = ("id", "book_name", "author", "published_year", "language", "cost")
    readonly_fields = ("id", )

admin.site.register(Book, BookAdmin)