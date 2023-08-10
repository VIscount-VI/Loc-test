from .models import BotUser, Inventory
from .serializers import BotUserSerializer, InventorySerializer
from rest_framework.generics import ListCreateAPIView
from django.views.generic.list import ListView

class BotUserApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class InventoryApiView(ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class List(ListView):
    queryset = BotUser.objects.all()
    template_name = 'user.html'

class List_2(ListView):
    queryset = Inventory.objects.all()
    template_name = 'list.html'