from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsView.as_view(), name='about_us'),
    path('faqs/', views.FaqsView.as_view(), name='faqs'),
]
