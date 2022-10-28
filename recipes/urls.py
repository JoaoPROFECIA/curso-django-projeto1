from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('', views.recipe),
    path('recipes/<int:id>/', views.recipe),  # <int:id> is a dynamic route
]
