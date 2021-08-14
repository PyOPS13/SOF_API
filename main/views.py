from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from .permissions import IsAuthorPermissions


class PermissionsMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermissions, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


class ProblemViewSet(PermissionsMixin, ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    http_method_names = ['GET', 'POST', 'PUT', 'DELETE']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(PermissionsMixin, ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class CommentViewSet(PermissionsMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



