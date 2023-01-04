from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('ClientList/', views.Client_list, name='Client_list'),
    path('ClientDetails/<int:Client_id>', views.Client_Details, name='Client_Details'),
    path('ClientUpdate/<int:Client_id>', views.Client_Update, name='Client_Update'),
    path('ClientDelete/<int:Client_id>', views.Client_Delete, name='Client_Delete'),
    path('DownloadingCSV/', views.DownloadingCSV, name='DownloadingCSV'),
    path('Search/', views.Search, name='Search'),

]