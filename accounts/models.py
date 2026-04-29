
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relaciona este perfil con un usuario de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
