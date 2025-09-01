# Removed incorrect import of 'request'
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from registrations.forms import ConcentratorOreFactoryForm
from registrations.models import ConcentratorOreFactory
from django.contrib import messages

# Create your views here.

class OreFactoryListView(ListView):
    model = ConcentratorOreFactory
    template_name = "pages/ore-factory/list.html"
    
    def get_queryset(self):
        return super().get_queryset().all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_queryset()
        return context
    
class OreFactoryDetailView(DetailView):
    model = ConcentratorOreFactory
    template_name = "pages/ore-factory/detail.html"
    context_object_name = "ore_factory"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_object()
        return context  
    
class OreFactoryCreateView(CreateView):
    template_name = "pages/ore-factory/form.html"
    form_class = ConcentratorOreFactoryForm
    model = ConcentratorOreFactory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = ConcentratorOreFactory.objects.all()
        return context
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("registrations:listOreFactory")

    def form_valid(self, form):
        messages.success(self.request, "Ore Factory created successfully.")
        return super().form_valid(form)
    


class OreFactoryUpdateView(UpdateView):
    model = ConcentratorOreFactory
    form_class = ConcentratorOreFactoryForm
    template_name = "pages/ore-factory/form.html"
    
    def get_success_url(self):
        return reverse_lazy("registrations:listOreFactory")
    
    def form_valid(self, form):
        messages.success(self.request, "Ore Factory updated successfully.")
        return super().form_valid(form) 

class OreFactoryDeleteView(DeleteView):
    model = ConcentratorOreFactory
    template_name = "pages/ore-factory/delete_confirm.html"
    success_url = reverse_lazy("registrations:listOreFactory")
    
    def get_success_url(self):
        return reverse_lazy("registrations:listOreFactory")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Ore Factory deleted successfully.")
        return super().delete(request, *args, **kwargs) 