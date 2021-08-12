from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from organization.models import Organization
from .permissions import OrganizationRegistrar
from .serializer import OrganizationSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, OrganizationRegistrar]

