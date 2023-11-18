from django.db import models
from .models import VMPlacementSpec ,VMs

from rest_framework import serializers
class VmSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMs
        fields = "__all__"


class Vmplacement(serializers.ModelSerializer):
    vm = models.OneToOneField(
        VMs,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    vm = VmSerializer()
    class Meta:
        model = VMPlacementSpec
        fields="__all__"

 