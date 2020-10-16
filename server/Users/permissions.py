from rest_framework import permissions


class UserIsOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_staff:
                return True
            else:
                return obj.user == request.user


class UserIsOwnerUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_staff:
                return True
            else:
                return obj.username == request.user.username


class UserOnlyViewPermissions(permissions.BasePermission):
    def has_permission(self, request, obj):
        if request.user.is_staff:
            return True
        else:
            return request.method in permissions.SAFE_METHODS
