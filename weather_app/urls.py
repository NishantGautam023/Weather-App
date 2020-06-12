from django.urls import path # to power our urlPattern we need to import path
from .views import HomePageView, AboutPageView # to ook in the current directory of views.py
urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    path('about/',AboutPageView.as_view(),name="about")
]
