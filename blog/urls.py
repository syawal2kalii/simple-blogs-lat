from django.urls import path
from . import views
urlpatterns = [
    path('article/', views.home, name='article'),
    path('addarticle/', views.addArticle, name='addarticle'),
    path('adduser/', views.addUser, name='adduser'),
    path('article/<str:pk>/', views.detailArticle, name='detail'),
    path('login/', views.login, name='login'),
]
