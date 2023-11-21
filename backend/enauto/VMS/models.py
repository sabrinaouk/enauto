from django.db import models
from .guestOS import guest_os 
import uuid 
from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField


class VMPlacementSpec(models.Model):
    idplacement= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
    ) 
    
    datastore=models.CharField(max_length=255)
    folder=models.CharField(max_length=255)

   
class VMCreateSpec (models.Model):
    VmGuestOS=(
        ('DOS', 'MS-DOS'),
        ('WIN_31' , 'Windows 3.1')

        )

    idspec= models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
     ) 
    # cluster=models.CharField(max_length=255)
    guest_OS=models.CharField(max_length=255,choices=VmGuestOS,default='MS-DOS')
    placement = models.OneToOneField(VMPlacementSpec, on_delete=models.CASCADE) 
    # datastore=models.CharField(max_length=255)
    # host=models.CharField(max_length=255)
    # resource_pool=models.CharField(max_length=255)


class VMs (models.Model):
        idvm= models.UUIDField( 
            primary_key = True, 
            default = uuid.uuid4, 
            editable = False) 
        spec = models.OneToOneField(VMCreateSpec, on_delete=models.CASCADE) 
# class VMCreateSpec (models.Model):
#     idvm= models.UUIDField( 
#          primary_key = True, 
#          default = uuid.uuid4, 
#          editable = False) 
#     spec = models.OneToOneField(, on_delete=models.CASCADE, blank=True, null=True) 
    # name = models.CharField(max_length=255)
    # guest_OS=models.CharField(max_length=255)
                              #choices=guest_os
     
     
    #vm = models.ForeignKey('VMs.idvm',on_delete=models.CASCADE,related_name="VMs")




# class VmHardwareBootDeviceType(Enum):
#         CDROM= 'CDROM'
#         DISK= 'DISK'
#         ETHERNET='ETHERNET'
#         FLOPPY='FLOPPY'
  

# class VmHardwareCdromHostBusAdapterType(Enum):
#     IDE='IDE',
#     SATA='SATA'
# class VmHardwareCdromDeviceAccessType(enumerate):
#     EMULATION='EMULATION'
#     PASSTHRU='PASTHRU'
#     PASSTHRU_EXCLUSIVE='PASSTHRU_EXCLUSIVE'


    
# class VmHardwareCdromBackingType(Enum):
#     ISO_FILE='CLIENT_DEVICE'
#     HOST_DEVICE='CLIENT_DEVICE'
#     CLIENT_DEVICE='CLIENT_DEVICE'


# class VMStoragePolicySpec(models.Model):
#     policy=models.CharField(max_length=255)
# # class VmHardwareDiskCreateSpec(models.Model):

# # class VmHardwareParallelCreateSpec(models.Model):

# class VmHardwareAdapterNvmeCreateSpec(models.Model):
#     bus =models.BigIntegerField()
#     pci_slot_number =models.BigIntegerField()

# class VmHardwareSerialCreateSpec(models.Model):
#         allow_guest_control =models.BooleanField(default=False)
#         start_connected =models.BooleanField(default=False)
#         yield_on_poll =models.BooleanField(default=False)


# class VmHardwareFloppyCreateSpec(models.Model):
#     allow_guest_control =models.BooleanField(default=False)
#     start_connected=models.BooleanField(default=False)

# class VmHardwareEthernetCreateSpec(models.Model):
#         allow_guest_control =models.BooleanField(default=False)
#         mac_address = models.CharField(max_length=255)
#         pci_slot_number=models.BigIntegerField()
#         start_connected=models.BooleanField(default=False)
#         upt_compatibility_enabled=models.BooleanField(default=False)
# class VmHardwareBootDeviceEntryCreateSpec(models.Model):
    
#     type=models.CharField(max_length=255,choices=VmHardwareBootDeviceType,default=VmHardwareBootDeviceType.CDROM)
 
# class VmHardwareCdromCreateSpec(models.Model):
#     allow_guest_control=models.BooleanField(default=False)
#     start_connected=models.BooleanField(default=False)
# class VmHardwareCdromBackingSpec(models.Model):

#     device_access_type=models.CharField(max_length=255,choices=VmHardwareCdromDeviceAccessType.choices)
#     host_device =models.CharField(max_length=255)
#     iso_file =models.CharField(max_length=255)
#     type=models.CharField(max_length=255,choices=VmHardwareCdromBackingType)






# class VmHardwareBootNetworkProtocol(enumerate):
#     IPV4 = 'IPV4'
#     IPV6 = 'IPV6'




# class VmHardwareBootType(enumerate):
#     BIOS = 'BIOS'
#     UEFI = 'UEFI'



# class VmHardwareDiskBackingType(enumerate):
#     VMDK_FILE='VMDK_FILE'





# class VmHardwareBootCreateSpec(models.Model):
#     delay= models.IntegerField(default=10000)
#     efi_legacy_boot =models.BooleanField(default=False)
#     enter_setup_mode =models.BooleanField(default=False)
#     network_protocol=models.CharField(max_length=10, choices= VmHardwareBootNetworkProtocol.choices)
#     retry =models.BooleanField(default=False)
#     retry_delay =models.IntegerField(default=10000) 
#     Type=models.CharField(max_length=10,choices= VmHardwareBootType.choices)


# class VmHardwareDiskBackingSpec(models.Model):
#     vmdk_file=models.CharField(max_length=255)
#     type=models.CharField(max_length=255,choices=VmHardwareDiskBackingType.choices)


# class VmHardwareCpuUpdateSpec(models.Model):
#     cores_per_socket=models.IntegerField()
#     count=models.IntegerField()
#     hot_add_enabled=models.BooleanField()
#     hot_remove_enabled=models.BooleanField()

# class VmHardwareSataAddressSpec(models.Model):
#     bus=models.BigIntegerField()
#     unit=models.BigIntegerField()

# class VmHardwareIdeAddressSpec(models.Model):
#     master=models.BooleanField()
#     primary=models.BooleanField()



# class VmHardwareDiskVmdkCreateSpec(models.Model):
#     capacity=models.BigIntegerField()
#     name=models.CharField(max_length=255)
