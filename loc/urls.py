from django.urls import path
from .views import BotUserApiView, InventoryApiView, List, List_2





urlpatterns = [
    path('bot-users', BotUserApiView.as_view()),
    path('inventory', InventoryApiView.as_view()),
    path('', List.as_view()),
    path('list/', List_2.as_view(), name='list'),
]