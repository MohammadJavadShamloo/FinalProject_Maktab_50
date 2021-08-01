from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('create/',
         views.CreateOrganizationView.as_view(),
         name='organization_create'),
    path('update/<int:pk>/',
         views.UpdateOrganizationView.as_view(),
         name='organization_update'),
    path('list/',
         views.ListOrganizationView.as_view(),
         name='organization_list'),
    path('detail/<int:pk>/',
         views.DetailOrganizationView.as_view(),
         name='organization_detail'),
    path('report/<int:pk>/',
         views.add_report,
         name='add_report'),
    path('province/list/',
         views.ListProvinceView.as_view(),
         name='province_list'),
    path('province/create/',
         views.CreateProvinceView.as_view(),
         name='province_create'),
    path('province/update/<int:pk>',
         views.UpdateProvinceView.as_view(),
         name='province_update'),
]
