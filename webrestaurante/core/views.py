from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Restaurante BitBrasas El mejor"})

class AboutPageView(TemplateView):
    template_name = "core/about.html"
