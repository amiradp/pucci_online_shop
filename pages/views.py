from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'pages/Home.html'
