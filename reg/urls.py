from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("account", views.account, name="account"),
    path("addparent", views.addparent, name="addparent"),
    path("deleteparent/<int:parent_id>/", views.delete_parent, name='delete_parent'),
    path('editparent/<int:parent_id>/', views.editparent, name='editparent'),
    path('', include("django.contrib.auth.urls")),
]

