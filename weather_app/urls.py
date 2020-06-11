from django.urls import path # to power our urlPattern we need to import path
from .views import HomePageView # to ook in the current directory of views.py
urlpatterns = [
    path('',HomePageView.as_view(),name="home")
]
