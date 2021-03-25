from django.shortcuts import render
from rest_framework import generics,  permissions
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer
# Create your views here.


class Postlist(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializers):
        poster = self.request.user
        serializers.save()


class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(id=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

        def perform_create(self, serializers):
            serializers.save(vote=self.request.user,
                             post=Post.objects.get(id=self.kwargs['pk']))
