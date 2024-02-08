from django.urls import path
from . import views

# urlpatterns = [
#     path('smoothie/', views.smoothie),
#     path('salad/', views.salad)
# ]

# Version 2

# urlpatterns = [
#     # path('smoothie/', views.smoothie),
#     # path('salad/', views.salad)
#     # path('<int:recipe>/', views.handle_recipe_with_number),
#     path('<str:recipe>/', views.handle_recipe)
# ]

# Version 3

urlpatterns = [
    # path('smoothie/', views.smoothie),
    # path('salad/', views.salad)
    path('', views.index),
    path('<int:recipe>/', views.handle_recipe_with_number),
    path('<str:recipe>/', views.handle_recipe, name='healthy-recipe')
]
