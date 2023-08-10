from .models import BotUser, Inventory
from rest_framework.serializers import ModelSerializer





class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name', 'username', 'user_id', 'created_at')

class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name', 'user_id', 'created_at', 'body')

