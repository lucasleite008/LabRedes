from django.db import models

# Create your models here.
class Leitura(models.Model):
    altura = models.FloatField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.data.strftime("%d-%m-%Y %H:%M")