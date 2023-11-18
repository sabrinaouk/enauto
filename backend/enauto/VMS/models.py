from django.db import models
from .guestOS import guest_os 
import uuid 
class VMs (models.Model):
    idvm= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    name = models.CharField(max_length=255)
    guest_OS=models.CharField(max_length=255,
                              #choices=guest_os
                              )




class VMPlacementSpec(models.Model):
     idplacement= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
     ) 
    
     datastore=models.CharField(max_length=255)
     folder=models.CharField(max_length=255)

     vm = models.OneToOneField(
        'VMs',  # Use a string reference to avoid circular import issues
        on_delete=models.CASCADE,
        #foreign_key=True,
    )
     #vm = models.ForeignKey('VMs.idvm',on_delete=models.CASCADE,related_name="VMs")