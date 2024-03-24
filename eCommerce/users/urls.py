from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("register/", views.registration.as_view(), name="register"),
]
