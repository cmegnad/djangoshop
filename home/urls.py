from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutUs, name='aboutus'),
    path('contact/', views.contact, name='contact')
]   