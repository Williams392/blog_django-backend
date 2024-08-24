from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET': # ttodos pueden acceder.
            return True 
        else:
            return request.user.is_staff # si tiene permiso de admin.