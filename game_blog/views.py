from django.views.generic import ListView, TemplateView
from .models import Post


class HomePageView(TemplateView):
    template_name = "home.html"


class NewsPageView(ListView):
    model = Post
    template_name = 'news.html'
