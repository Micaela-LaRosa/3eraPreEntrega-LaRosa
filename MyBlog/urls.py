from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="Home"),
    path('users/', users, name="Users"),
    path('posts/', posts, name="Posts"),
    path('comments/', comments, name="Comments"),
    path('categories/', categories, name="Categories"),
    path('usersForm/', usersForm, name="UsersForm"),
    path('commentsForm/', commentsForm, name="CommentsForm"),
    path('postsForm/', postsForm, name="PostsForm"),
    path('categoriesForm/', categoriesForm, name="CategoriesForm"),
    path('userSearch/', userSearch, name="UserSearch"),
    path('search/', search, name="search"),
]