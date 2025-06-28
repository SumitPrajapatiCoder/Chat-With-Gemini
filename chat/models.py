from django.db import models

class ChatMessage(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    model_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"