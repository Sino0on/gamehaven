from django.urls import path
from game.views import home


urlpatterns = [
    path('', home, name='home')
]
