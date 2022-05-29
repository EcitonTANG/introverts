from django.contrib import admin
from django.urls import path

from introverts.views import *

urlpatterns = [
    path('mealsitems/', MealItemsView.as_view()),
    path('categoryitems/', CategoryItemsView.as_view()),
    path('meals/', MealsView.as_view())
]