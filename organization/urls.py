from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('create/',
         views.CreateOrganizationView.as_view(),
         name='create_organization'),
    path('update/<int:pk>/',
         views.UpdateOrganizationView.as_view(),
         name='update_organization'),
    path('list/',
         views.ListOrganizationView.as_view(),
         name='list_organization'),
    path('detail/<int:pk>/',
         views.DetailOrganizationView.as_view(),
         name='detail_organization'),
    path('report/<int:pk>/',
         views.add_report,
         name='add_report'),
]
