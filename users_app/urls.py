from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.get_users),
    path('add_user', views.add_users)
]
