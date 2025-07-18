# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('newar/', views.newar, name='newar'),
    path('chhetri/', views.chhetri, name='chhetri'),
    path('rai/', views.rai, name='rai'),
    path('sherpa/', views.sherpa, name='sherpa'),
    path('gurung/', views.gurung, name='gurung'),
    path('tharu/', views.tharu, name='tharu'),

]

