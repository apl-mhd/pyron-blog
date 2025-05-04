from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.


class PostAPIView(APIView):

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostListAPIView(ListAPIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDeleteAPIView(DestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()


@api_view(['GET'])
def index(request):

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):

    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        # print(type(request.data))
        # print(type(serializer.validated_data))
        # serializer.save(**request.data, author=request.user)
        # serializer.save(author=request.user, title="no title")
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
