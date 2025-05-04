from django.urls import path
from .import views


urlpatterns = [

    path('', views.PostListAPIView.as_view(), name='index'),
    path('create/', views.PostAPIView.as_view(), name='api_post_create'),
    path('<int:pk>/', views.PostUpdateAPIView.as_view(),
         name='api_post_update'),
    path('<int:pk>/', views.PostDeleteAPIView.as_view(),
         name='api_post_delete'),
]
