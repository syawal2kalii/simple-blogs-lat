from django.shortcuts import render, redirect
import blog.models as datadb
import sys
from .forms import UserForm, ArticleForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import article
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
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
    # print()
    return render(request, 'home.html', context)


def detailArticle(request, pk):
    print(pk)
    # sys.exit()
    context = {
        'posts': datadb.article.objects.get(id=pk)
    }
    return render(request, 'detail.html', context)


def addArticle(request):
    if request.method == 'POST':
        # ArticleForm(request.POST, request.FILES)
        print('data ', make_password(str(request.FILES['imgurl'])))
        article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            imgurl=request.FILES['imgurl'],
        )
    context = {
        'article_form': ArticleForm()}

    return render(request, 'addarticle.html', context)


def hapusArticle(request, id):
    art = article.objects.get(id=id)
    art.delete()
    return redirect('article')


def updateArticle(request, id):
    art = article.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=art)
    # data = {
    #     'nama':}
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            return redirect('article')
        else:
            print("gagal")
            return redirect('article')
    context = {
        'article_form': ArticleForm(request.POST or None, instance=art),
        'article': art
    }
    return render(request, 'update.html', context)


def addUser(request):
    if request.method == 'POST':
        User.objects.create(
            username=request.POST['username'],
            password=make_password(request.POST['password']),
            email=request.POST['email'],

        )

    return render(request, 'adduser.html', context={'user_form': UserForm()})


def login(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
    return render(request, 'login.html', context={'login_form': LoginForm()})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('article')
