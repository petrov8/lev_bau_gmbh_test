

from django.urls import path, include
from app_main.views import show_main_page


urlpatterns = [

    path("", show_main_page, name="home")
]
