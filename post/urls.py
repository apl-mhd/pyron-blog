from django.urls import path
from .import views


urlpatterns = [
    path('', views.PostListCreateAPIView.as_view(),
         name='api_posts_list_create'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(),
         name='api_posts_retrieve_update_destroy'),
]
