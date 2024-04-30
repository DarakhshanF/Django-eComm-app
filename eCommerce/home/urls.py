from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about-us'),
]
