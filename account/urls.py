from django.urls import path
from . import views


urlpatterns = [
    # Region
    path('regions/', views.RegionListAPIView.as_view()),
    path('regions/<int:pk>', views.RegionDetailAPIView.as_view()),

    # District
    path('districts/', views.DistrictListAPIView.as_view()),
    path('districts/<int:pk>', views.DistrictDetailAPIView.as_view()),
]
