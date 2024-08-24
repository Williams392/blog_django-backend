
from rest_framework.permissions import BasePermission


# Permiso para los endpoints para category:
class IsAdminOrReadOnly(BasePermission): 
    def has_permission(self, request, view):
        if request.method == 'GET': # para cualquir usuario
            return True
        else:
            return request.user.is_staff # si es administrador si puede acceder put, delete, etc.