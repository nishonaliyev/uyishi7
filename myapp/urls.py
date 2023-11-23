from django.urls import path
from .views import main, details
urlpatterns = [
    path('', main, name='main'),
    path('<int:id</', details, name="details"),
]