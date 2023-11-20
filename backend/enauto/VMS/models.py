from django.db import models
from .guestOS import guest_os 
import uuid 


 

class placement(models.Model):
    idplacement= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
    ) 
    
    datastore=models.CharField(max_length=255)
    folder=models.CharField(max_length=255)

   
class spec(models.Model): 
    idspec= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
     ) 

    guest_OS=models.CharField(max_length=255)
    placement = models.OneToOneField(placement, on_delete=models.CASCADE, blank=True, null=True) 

class VMs (models.Model):
    idvm= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    spec = models.OneToOneField(spec, on_delete=models.CASCADE, blank=True, null=True) 
    # name = models.CharField(max_length=255)
    # guest_OS=models.CharField(max_length=255)
                              #choices=guest_os
     
     
    #vm = models.ForeignKey('VMs.idvm',on_delete=models.CASCADE,related_name="VMs")