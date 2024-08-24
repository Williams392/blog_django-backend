from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = [OrderingFilter, DjangoFilterBackend] # sistema de orden.
    ordering = ['-created_at']

    filterset_fields = ['post'] # filtrar por categorias  de un post


'''
_ Sistema de ordenamiento:
1. ordering = ['-created_at']
. devuelve de mas nuevo a mas viejo

1. ordering = ['created_at']
. devuelve de mas viejo  a mas nuevo


_ Filtrado por id del post:
http://127.0.0.1:8000/api/comments/?post=1

'''