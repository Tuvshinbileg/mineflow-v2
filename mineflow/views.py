
from django.shortcuts import render
# Removed incorrect import of 'request'
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from registrations.forms import ConcentratorOreFactoryForm
from registrations.models import ConcentratorOreFactory

def index(request):
    data = ConcentratorOreFactory.objects.all()
    context = {
        'layout': 'default',
        'data':data
        
    }
    return render(request, 'pages/index.html', context)



