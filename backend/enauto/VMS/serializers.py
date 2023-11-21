from django.db import models
from .models import VMCreateSpec,VMPlacementSpec,VMs
from rest_framework import serializers

class placementSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = VMPlacementSpec
        fields="__all__"

class specSerializer(serializers.ModelSerializer):
    placement = models.OneToOneField(
        VMPlacementSpec,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # placement=placementSerializer()
    class Meta:
        model = VMCreateSpec
        fields="__all__"
        read_only_fields = ['guest_OS']

    # def create(self, validated_data):
    #     print('piiiiiiiiiiiiw')
    #     print(validated_data)
    #     print(validated_data["spec"]["placement"])
    #     datta=validated_data.get("spec")

    #     placementt=VMPlacementSpec.objects.create(**validated_data["spec"]["placement"])

    #     datta.pop('placement',None)
    #     print(datta)
    #     specc=VMCreateSpec.objects.create(**datta,placement=placementt)
    #     validated_data["spec"]=specc
    #     print(specc)
    #     print('ddddddddddddddddddddddddddd')
    #     return super().create(validated_data)
    

# class VmHardwareBootDeviceEntryCreateSpec(serializers.ModelSerializer):
#     idhbec = models.OneToOneField(
#         VmHardwareBootDeviceEntryCreateSpec,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     # placement=placementSerializer()
#     class Meta:
#         model = spec
#         fields="__all__"



class VmSerializer(serializers.ModelSerializer):
    spec = models.OneToOneField(
        VMCreateSpec,
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
        print('hadi datttta',datta)
        placementt=VMPlacementSpec.objects.create(**validated_data["spec"]["placement"])

        datta.pop('placement',None)
        print(datta)
        specc=VMCreateSpec.objects.create(**datta,placement=placementt)
        validated_data["spec"]=specc
        print(specc)
        print('ddddddddddddddddddddddddddd')
        return super().create(validated_data)
    







 