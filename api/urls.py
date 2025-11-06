from django.urls import path
from . import views

urlpatterns = [
    path("/<str:ticket>/", views.stockDetailView),
]