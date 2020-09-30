from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, views, object, request):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.author == request.user