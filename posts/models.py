# 1:
from django.db import models
from django.db.models import SET_NULL

from users.models import User
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/images/') # se crea automatico
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True) # pk
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True) # 

    def __str__(self):
        return self.title # con esto evitamos que se vea (POST OBJECT)


'''
. se pone SET_NULL para que cuando el user borre o se 
desvincule no se borre el objeto POST.
'''