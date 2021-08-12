from rest_framework.permissions import BasePermission


class OrganizationRegistrar(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.registrar == request.user
