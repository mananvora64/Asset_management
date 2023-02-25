from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('indexnew', views.Indexnew, name="indexnew"),
    path('front', views.Fronts, name="front"),
    path('add', views.add, name='add'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'), 
    path('login', views.Loginuser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('front-pdf', views.Fronts_pdf, name="front_pdf"),
    path('registration', views.Registrationpage, name="registration"),
    path('modal', views.modalUser, name="modal"),

]