from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("<str:code>/", views.go_to_url, name="go_to_url"),
]