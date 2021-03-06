from django.urls import path
from .views import HomePageView, NewsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/', NewsPageView.as_view(), name='news'),
]