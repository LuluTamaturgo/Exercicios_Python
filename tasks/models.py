from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=255)  # Título da tarefa
    description = models.TextField(blank=True)  # Descrição opcional
    created_at = models.DateTimeField(default=now, editable=False)  # Data e hora automática
    completed = models.BooleanField(default=False)  # Status da tarefa
    

    def __str__(self):
        return self.title



