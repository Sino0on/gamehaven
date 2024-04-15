from api.serializers import ApplicationSerializer
from rest_framework.generics import CreateAPIView
from game.models import Application


class ApplicationCreateView(CreateAPIView):
    model = Application
    serializer_class = ApplicationSerializer

