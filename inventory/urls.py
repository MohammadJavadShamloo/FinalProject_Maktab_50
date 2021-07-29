from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('create/',
         views.CreateProductView.as_view(),
         name='create_product'),
    path('list/',
         views.ListProductView.as_view(),
         name='list_product'),
    path('update/<int:pk>/',
         views.UpdateProductView.as_view(),
         name='update_product'),
    path('detail/<int:pk>/',
         views.DetailProductView.as_view(),
         name='detail_product'),
]
