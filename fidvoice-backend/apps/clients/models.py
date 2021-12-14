from django.db import models
from user.models import User

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
