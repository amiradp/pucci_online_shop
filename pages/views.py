from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'pages/Home.html'


class AboutUsView(generic.TemplateView):
    template_name = 'pages/About_us.html'


class FaqsView(generic.TemplateView):
    template_name = 'pages/faqs.html'
