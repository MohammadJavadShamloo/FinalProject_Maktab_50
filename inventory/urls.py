from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('create/',
         views.CreateProductView.as_view(),
         name='product_create'),
    path('list/',
         views.ListProductView.as_view(),
         name='product_list'),
    path('update/<int:pk>/',
         views.UpdateProductView.as_view(),
         name='product_update'),
    path('detail/<int:pk>/',
         views.DetailProductView.as_view(),
         name='product_detail'),
]
