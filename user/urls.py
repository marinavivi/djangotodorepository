from user import views
from django.urls import path, include


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('users/', views.UserListAPI.as_view(), name='users'),
    path('users/<int:pk>/', views.UserRetrieveView.as_view(), name='user'),
    
]