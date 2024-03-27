from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.registration.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
