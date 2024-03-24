from django.urls import path
from users import views
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
    path("register/", views.registeration.as_view(), name="register"),
]
