from django.db import models

class BotUser(models.Model):
    user_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
         return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=200, blank=True)
    user_id = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name