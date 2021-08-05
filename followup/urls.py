from django.urls import path

from . import views

app_name = 'followup'

urlpatterns = [
    path('report/<int:pk>/',
         views.add_report,
         name='add_report'),
]
