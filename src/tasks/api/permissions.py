from rest_framework import permissions


class ProjectsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'destroy']:
            return obj.user == request.user or request.user.is_superuser

        return False
