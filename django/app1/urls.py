from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksView.as_view(), name='books-list'),    # [GET] books list
    path('create/', views.BooksView.as_view(), name='create-books-record'),    # [POST] create books record
    path('<int:id>/update/', views.BooksView.as_view(), name='update-books-record'),    # [PUT] update books record
    path('<int:id>/delete/', views.BooksView.as_view(), name='delete-books-record'),    # [DELETE] delete books record
    path('<int:id>/show/', views.BookRecordView.as_view(), name='show-book-record'),    # [GET] show book record

]