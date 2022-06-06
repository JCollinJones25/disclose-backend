from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name="location_detail"),
    path('locations/new/', views.LocationCreate.as_view(), name='location_create'),
]