from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True # ttodo el mundo puede pasar y crear.
        else:
            id_comment = view.kwargs['pk'] # id del comentario.
            comment = Comment.objects.get(pk=id_comment) # una peticion ala base de datos de ese comentario.

            id_user = request.user.pk # el id del usuario q esta ejecuntado la peticion.
            id_user_comment = comment.user_id # comparamos

            if id_user == id_user_comment:
                return True # si el id es del usuario podra eliminar y 
            
            return False # si no es el propetario no van a tener permiso de eliminar oh actualizar.
        

''''
_ Traduccion:
1. IsOwnerOrReadAndCreateOnly:  
Si eres el propietario, podrás hacer todo, y si no, 
solo podrás leer y crear nuevos registros.

_ Apuntes:

1. view.kwargs se utiliza para acceder a los parámetros 
de la URL que se han capturado en la vista.

obtiene el valor del parámetro pk de la URL, que se utiliza 
para identificar un comentario específico. Este valor se usa
luego para recuperar el comentario correspondiente de la base 
de datos y verificar si el usuario actual es el propietario del
comentario.

'''