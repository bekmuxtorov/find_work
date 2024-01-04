from django.urls import path
from . import views


urlpatterns = [
    # Region
    path('regions/', views.RegionListAPIView.as_view()),
    path('regions/<int:pk>/', views.RegionDetailAPIView.as_view()),

    # District
    path('districts/', views.DistrictListAPIView.as_view()),
    path('districts/<int:pk>/', views.DistrictDetailAPIView.as_view()),

    # User Registration
    path('auth/register/', views.UserRegistrationAPIView.as_view()),

    # User Login
    path('auth/login/', views.UserLoginAPIView.as_view()),

    # Change password
    path('auth/change/password/', views.ChangePasswordAPIView.as_view()),

    # Employer
    path('employers/', views.EmployerListAPIView.as_view()),
    path('employers/<int:pk>/', views.EmployerDetailAPIView.as_view()),
]
