from django.urls import path
from game.views import home
from api.views import ApplicationCreateView


urlpatterns = [
    path('', home, name='home'),


    path('api/application/create/', ApplicationCreateView.as_view())
]
