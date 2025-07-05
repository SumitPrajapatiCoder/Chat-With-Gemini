from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prompt = models.TextField()
    response = models.TextField()
    model_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       username = self.user.username if self.user else "UnknownUser"
       safe_timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M') if self.timestamp else "NoTime"
       return f"{username} - {self.model_name} @ {safe_timestamp}"

