from django.urls import path
from registrations.views import OreFactoryFormView
app_name = 'registrations'

urlpatterns = [
    path('ore-factory/create', OreFactoryFormView.as_view(), name="createOreFactory"),
    path('ore-factory/<int:pk>', OreFactoryFormView.as_view(), name="detailOreFactory")
]