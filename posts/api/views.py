# 3:
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly] # post, delete solo admin.
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend] # Estos filtros para q solo me devuela por categoria - django y todo me debe de mostrar django.
    filterset_fields = ['category', 'category__slug'] # 2 filtros: id y slug

'''
_ filtros: id y slug

1. Filtro por id:
http://127.0.0.1:8000/api/posts/?category=1

2. Filtro por slug:
http://127.0.0.1:8000/api/posts/?category__slug=react

'''