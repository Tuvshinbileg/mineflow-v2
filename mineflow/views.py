
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



class OreFactoryFormView(SingleObjectMixin, FormView):
    template_name = "pages/ore-factory/detail.html"
    form_class =ConcentratorOreFactoryForm 
    model = ConcentratorOreFactory

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        data = ConcentratorOreFactory.objects.all()
        return reverse("index", kwargs={"pk": self.object.pk, "data": data})