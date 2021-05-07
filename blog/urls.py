from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='article'),
    path('addarticle/', views.addArticle, name='addarticle'),
    path('adduser/', views.addUser, name='adduser'),
    path('article/<str:pk>/', views.detailArticle, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<str:id>', views.updateArticle, name='update'),
    path('hapus/<str:id>', views.hapusArticle, name='hapus'),
]
