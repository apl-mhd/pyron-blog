from .serializers import PostSerializer
from .models import Post
from accounts.permissions import IsOwner
from django.db.models import Q
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 1000

    def get_paginated_response(self, data):
        return Response({
            'total': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomLimitOffsetPagination  # LimitOffsetPagination
    permission_classes = [AllowAny, IsAuthenticated]

    def get_queryset(self):
        queryset = Post.objects.all()

        title = self.request.query_params.get("title", "")
        content = self.request.query_params.get("content", "")

        if title and content:
            queryset = queryset.filter(Q(title__icontains=title)
                                 | Q(content__icontains=content))
        elif title:
            queryset = queryset.filter(title__icontains=title)
        elif content:
            queryset = queryset.filter(content__icontains=content)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        isinstance = self.get_object()
        perv_image = isinstance.image

        serializer = self.get_serializer(
            instance=isinstance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        try:

            if serializer.validated_data['image'] and perv_image.path and os.path.exists(perv_image.path):
                os.remove(perv_image.path)
        except Exception as e:
            print(f"Error deleting old image: {e}")

        return Response(data={"message": "Post Updated Successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        isinstance = self.get_object()
        image_path = isinstance.image
        isinstance.delete()

        try:
            if image_path and os.path.exists(image_path.path):
                os.remove(image_path.path)
        except Exception as e:
            print(f"Error deleting image: {e}")

        return Response(data={"message": "Post Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsOwner()]
        return [AllowAny()]
