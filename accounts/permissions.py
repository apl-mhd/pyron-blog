from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            # Read-only permissions are allowed for any request
            return True

        return obj.author == request.user
