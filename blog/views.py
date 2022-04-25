from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post-new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post-edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = "about.html"

class ProjectsPageView(TemplateView):
    template_name = 'proj.html'

class CcsPageView(TemplateView):
    template_name = 'ccs.html'

class SendOrderPageView(TemplateView):
    template_name = 'buyurtma.html' 

class ServicePageView(TemplateView):
    template_name = 'services.html'

class SplashScreenPageView(TemplateView):
    template_name = 'index.html'



