from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("calendar", views.calendar, name="calendar"),
    path("housework_registration", views.housework_registration, \
         name="housework_registration"),
]
