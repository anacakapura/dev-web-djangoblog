from django.urls import path
from .views import (
    ArtikelListView, 
    ArtikelDetailView, 
    ArtikelCreateView,
    ArtikelManageListView,
    ArtikelDeleteView,
    ArtikelUpdateView
)

urlpatterns = [
    path('manage/update/<int:pk>/', ArtikelUpdateView.as_view(), name='artikel_update'),
    path('manage/delete/<int:pk>/', ArtikelDeleteView.as_view(), name='artikel_delete'),
    path('manage/', ArtikelManageListView.as_view(), name='artikel_manage'),
    path('create/', ArtikelCreateView.as_view(), name='artikel_create'),
    path('detail/<str:slug>', ArtikelDetailView.as_view(), name='artikel_detail'),
    path('<str:kategori>/<int:page>', ArtikelListView.as_view(), name='artikel_kategori'),
    path('<str:kategori>', ArtikelListView.as_view(), name='artikel_list')
]