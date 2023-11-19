from django.db import models
from .models import VMs, spec,placement

from rest_framework import serializers

class placementSerializer(serializers.ModelSerializer):
  
    class Meta:
        model =placement
        fields="__all__"

class specSerializer(serializers.ModelSerializer):
    placement = models.OneToOneField(
        placement,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # placement=placementSerializer()
    class Meta:
        model = spec
        fields="__all__"

    
class VmSerializer(serializers.ModelSerializer):
    spec = models.OneToOneField(
        spec,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # spec=specSerializer()
    class Meta:
        model = VMs
        fields = "__all__"
    







 