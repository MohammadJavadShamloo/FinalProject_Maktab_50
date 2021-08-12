from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'organization_api'

router = routers.DefaultRouter()
router.register('organization_api', views.OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
