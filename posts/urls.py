from django.urls import path
from .views import test
app_name = "posts"

urlpatterns = [
    path('', test),
]
