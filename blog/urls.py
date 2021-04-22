from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('home/', views.home),
=======
urlpatterns = [
    path('home/', views.home, name='home'),
>>>>>>> d169c2856a921a1ca50a36f3000384ea199a4c0e
]
