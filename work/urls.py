from django.urls import path
from . import views


urlpatterns = [
    # Category
    path('categories/create/', views.CategoryCreateAPIView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    path('categories/<int:pk>/update/', views.CategoryUpdateAPIView.as_view()),
    path('categories/<int:pk>/delete/', views.CategoryDeleteAPIView.as_view()),

    # SubCategory
    path('subcategories/create/', views.SubCategoryCreateAPIView.as_view()),
    path('subcategories/', views.SubCategoryListAPIView.as_view()),
    path('subcategories/<int:pk>/', views.SubCategoryDetailAPIView.as_view()),
    path('subcategories/<int:pk>/update/', views.SubCategoryUpdateAPIView.as_view()),
    path('subcategories/<int:pk>/delete/', views.SubCategoryDeleteAPIView.as_view()), 

    # Work
    path('works/create/', views.WorkCreateAPIView.as_view()),
    path('works/', views.WorkListAPIView.as_view()),
    path('works/<int:pk>/', views.WorkDetailAPIView.as_view()),
    path('works/<int:pk>/update/', views.WorkUpdateAPIView.as_view()),
    path('works/<int:pk>/delete/', views.WorkDeleteAPIView.as_view()), 
]
