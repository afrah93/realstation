
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('Plogin/', views.passengerLogin, name='Plogin'),
    path('Alogin/', views.adminLogin, name='Alogin'),
    path('infopassenger/', views.infopassenger, name='infopassenger'),
    path('traininfo/', views.traininfo, name='traininfo'),
]