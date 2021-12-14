from django.db import models
from apps.user.models import User

class Client(models.Model):
    created_by = models.ForeignKey(User,related_name='client',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    org_number = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    zipcode =  models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    contact_person =  models.CharField(max_length=200, blank=True, null=True)
    contact_reference =  models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
