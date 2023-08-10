from django.contrib import admin
from .models import BotUser, Inventory
# Register your models here.
class CattegoryAdmin(admin.ModelAdmin):
    list_display = ['body']
admin.site.register(BotUser)
admin.site.register(Inventory)