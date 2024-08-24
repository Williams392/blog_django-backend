# 4:
from rest_framework import serializers
from posts.models import Post

from users.api.serializers import UserSerializer # yo
from categories.api.serializers import CategorySerializer # yo

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer() # para obtener toda la info de user en objeto en el json de posts.
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id','title', 'content', 'slug', 'miniature', 
                  'created_at', 'published', 'user', 'category']