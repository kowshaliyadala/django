from django.urls import path
from auth.views import register, fetchUsers, login

urlpatterns = [
    path('register', register),
    path('fetchUsers', fetchUsers),
    path('login', login)
]