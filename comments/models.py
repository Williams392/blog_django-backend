from django.db import models
from django.db.models import CASCADE
from users.models import User
from posts.models import Post


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=CASCADE, null=True) # pk
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True) # pk

    def __str__(self):
        return self.content # con esto evitamos que se vea (OBJECT)
    
'''
_ Ahora con (on_delete=CASCADE) cuando un usuario es eliminado el 
comentario sí queremos que se elimine de manera cascada todos sus 
comentarios.
'''