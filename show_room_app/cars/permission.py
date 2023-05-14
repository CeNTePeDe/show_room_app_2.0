from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access only to admin users or read only.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_staff
