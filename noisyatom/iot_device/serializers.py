from rest_framework import serializers
from iot_device.models import IoTMachine, LANGUAGE_CHOICES, STYLE_CHOICES


class IoTMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = IoTMachine
        fields = ('device_id', 'device_name', 'local_ip', 'device_owner', 'multicast_address')


    def create(self, validated_data):
        """
        Create and return a new `IoT Device` instance, given the validated data.
        """
        return IoTMachine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `IoT Device` instance, given the validated data.
        """
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.device_name = validated_data.get('device_name', instance.device_name)
        instance.local_ip = validated_data.get('local_ip', instance.local_ip)
        instance.multicast_address = validated_data.get('multicast_address', instance.multicast_address)
        instance.bluetooth_address = validated_data.get('bluetooth_address', instance.bluetooth_address)
        instance.save()
        return instance
