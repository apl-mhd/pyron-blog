from .serializers import PostSerializer
from .models import Post
from accounts.permissions import IsOwner
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostListAPIView(ListAPIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveAPIView(APIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class PostDeleteAPIView(DestroyAPIView):
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
