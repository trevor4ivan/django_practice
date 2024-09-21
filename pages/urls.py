from django.urls import path
from .views import new_home_page
urlpatterns=[
    path("", new_home_page)
]