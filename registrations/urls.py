from django.urls import path
from registrations.views import (OreFactoryListView,
                                 OreFactoryDetailView,
                                 OreFactoryCreateView,
                                 OreFactoryUpdateView,
                                OreFactoryDeleteView
                                 )
app_name = 'registrations'

urlpatterns = [
    path('ore-factory/create', OreFactoryCreateView.as_view(), name="createOreFactory"),
    path('ore-factory', OreFactoryListView.as_view(), name="listOreFactory"),
    path('ore-factory/<int:pk>', OreFactoryDetailView.as_view(), name="detailOreFactory"),
    path('ore-factory/<int:pk>/edit', OreFactoryUpdateView.as_view(), name="editOreFactory"),
    path('ore-factory/<int:pk>/delete', OreFactoryDeleteView.as_view(), name="deleteOreFactory")
]