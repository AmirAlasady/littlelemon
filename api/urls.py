
from django.urls import path
from . import views
urlpatterns = [
    path('food/',views.handler),
    path('foods/<int:pk>',views.slk)
]