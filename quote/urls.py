from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('create/',
         views.QuoteCreateView.as_view(),
         name='quote_create'),
    path('list/',
         views.QuoteListView.as_view(),
         name='quote_list'),
    path('detail/<int:pk>/',
         views.QuoteDetailView.as_view(),
         name='quote_detail'),
    path('pdf/<int:quote_id>/',
         views.quote_pdf,
         name='quote_pdf'),
    path('email/<int:quote_id>/<int:organization_id>/',
         views.send_quote_to_organization,
         name='send_mail'),
]
