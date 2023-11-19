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
    class Meta:
        model = VMs
        fields = "__all__"

    def create(self, validated_data):
        print('piiiiiiiiiiiiw')
        print(validated_data)
        print(validated_data["spec"]["placement"])
        datta=validated_data.get("spec")

        placementt=placement.objects.create(**validated_data["spec"]["placement"])

        datta.pop('placement',None)
        print(datta)
        specc=spec.objects.create(**datta,placement=placementt)
        validated_data["spec"]=specc
        print(specc)
        print('ddddddddddddddddddddddddddd')
        return super().create(validated_data)
    







 