from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Post, Comment, Category
from .forms import UsersForm, PostsForm, CommentsForm, CategoriesForm

# Create your views here.

def home(req):
    return render(req, "home.html", {})

def users(req):
    return render(req, "users.html", {})

def posts(req):
    return render(req, "posts.html", {})

def comments(req):
    return render(req, "comments.html", {})

def categories(req):
    return render(req, "categories.html", {})

def usersForm(req):
    if req.method == "POST":
        myForm= UsersForm(req.POST) 
        print(myForm)
        if myForm.is_valid(): 
            information = myForm.cleaned_data
            user = User(name=information['name'], last_name=information['last_name'], email=information['email']) 
            user.save()
            return render(req, 'home.html') 
    else: myForm=UsersForm() 
    return render(req, 'usersForm.html', {'myForm':myForm})

def postsForm(req):
    if req.method == "POST":
        myForm = PostsForm(req.POST)
        print(myForm)
        if myForm.is_valid():
            information = myForm.cleaned_data
            post = Post(title=information['title'], text=information['text'], publish_date=information['publish_date'], modified_date=information['modified_date'])
            post.save()
            return render (req, 'home.html')
    else: myForm= PostsForm()
    return render(req, "postsForm.html", {'myForm':myForm})

def commentsForm(req):
    if req.method == "POST":
        myForm= CommentsForm(req.POST) 
        print(myForm)
        if myForm.is_valid(): 
            information = myForm.cleaned_data
            comment = Comment(author=information['author'], created_date=information['created_date'], text=information['text']) 
            comment.save()
            return render(req, 'home.html')
    else: myForm=CommentsForm()
    return render(req, 'commentsForm.html', {'myForm':myForm})

def categoriesForm(req):
    if req.method == "POST":
        myForm= CategoriesForm(req.POST) 
        print(myForm)
        if myForm.is_valid(): 
            information = myForm.cleaned_data
            category = Category(name=information['name'])
            category.save()
            return render(req, 'home.html') 
    else: myForm=CategoriesForm() 
    return render(req, 'categoriesForm.html', {'myForm':myForm})

def userSearch(req):
    return render(req, 'userSearch.html')

def search(req):
    if req.GET["name"]:
        name= req.GET["name"]
        users = User.objects.filter(name__icontains=name)
        return render(req, 'resultSearch.html', {"users": users, "name": name})
    else: answer = "Please sent some info"
    return HttpResponse(answer)


