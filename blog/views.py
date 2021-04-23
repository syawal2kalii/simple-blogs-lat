from django.shortcuts import render
import blog.models as datadb
import sys
from .forms import UserForm, ArticleForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import article
# Create your views here.


def home(request):
    context = {
        'title': 'Home',
        # dari database
        'posts': datadb.article.objects.all()

        # 'posts': [
        #     {
        #         'posted': 'syawal',
        #         'title': 'artikel1'
        #     },
        #     {
        #         'posted': 'anu',
        #         'title': 'artikel 2'
        #     },
        #     {
        #         'posted': 'syawal',
        #         'title': 'artikel 3'
        #     }
        # ]
    }
    print(len(context['posts']))
    return render(request, 'home.html', context)


def detailArticle(request, pk):
    print(pk)
    # sys.exit()
    context = {
        'posts': datadb.article.objects.get(id=1)
    }
    return render(request, 'detail.html', context)


def addArticle(request):
    if request.method == 'POST':
        article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
    context = {
        'article_form': ArticleForm()}

    return render(request, 'addarticle.html', context)


def addUser(request):
    if request.method == 'POST':
        User.objects.create(
            username=request.POST['username'],
            password=make_password(request.POST['password']),
            email=request.POST['email']
        )

    return render(request, 'adduser.html', context={'user_form': UserForm()})


def login(request):
    return render(request, 'login.html')
