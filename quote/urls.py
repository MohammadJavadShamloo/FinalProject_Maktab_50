from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('create/',
         views.QuoteCreateView.as_view(),
         name='create_quote'),
]